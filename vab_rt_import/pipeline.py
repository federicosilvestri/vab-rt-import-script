"""Main pipeline class"""
import importlib
import logging
from typing import Callable

import pandas as pd

logger = logging.getLogger(__name__)

REQUIRED_INITIAL_FUNCTION = "init"
REQUIRED_PROCESS_FUNCTION = "process"
REQUIRED_IMPORT_FUNCTION = "import_entity"

INITIAL_FUNCTIONS = []

PROCESS_FUNCTIONS = [
    "vab_rt_import.process.fiscal",
    "vab_rt_import.process.subscription",
]

IMPORT_FUNCTIONS = [
    "vab_rt_import.importing.fiscal",
    "vab_rt_import.importing.subscription",
]


class PipelineConfigError(Exception):
    """Raised when pipeline modules are misconfigured"""


class Pipeline:
    """Main pipeline class"""

    def __init__(self, source_fun: Callable[[], pd.DataFrame]):
        self._initial_functions = []
        self._processing_functions = []
        self._importing_functions = []
        self._source_fun = source_fun
        self._validate_functions()

    def _validate_functions(self):
        """Check that required functions exist in every module"""
        missing = []

        stages = [
            (INITIAL_FUNCTIONS,  REQUIRED_INITIAL_FUNCTION,  self._initial_functions),
            (PROCESS_FUNCTIONS,  REQUIRED_PROCESS_FUNCTION,  self._processing_functions),
            (IMPORT_FUNCTIONS,   REQUIRED_IMPORT_FUNCTION,   self._importing_functions),
        ]

        for module_paths, required_fn, fn_list in stages:
            for module_path in module_paths:
                try:
                    module = importlib.import_module(module_path)
                    if not hasattr(module, required_fn):
                        missing.append(f"{module_path}: missing '{required_fn}'")
                    else:
                        fn_list.append(getattr(module, required_fn))
                except ModuleNotFoundError:
                    missing.append(f"{module_path}: module not found")

        if missing:
            raise PipelineConfigError(
                "Pipeline misconfigured:\n" + "\n".join(f"  - {m}" for m in missing)
            )

    def _run_stage(self, fn_list: list, stage_name: str):
        """Run all functions in a stage sequentially"""
        logger.info("Starting stage: %s", stage_name)
        for fn in fn_list:
            logger.info("Running %s", fn.__name__)
            fn()

    def _run_process_stage(self, source: pd.DataFrame):
        """Run all process functions, passing source DataFrame to each"""
        logger.info("Starting stage: process")
        for fn in self._processing_functions:
            logger.info("Running %s", fn.__name__)
            fn(source)

    def run(self):
        """Execute full pipeline: init → (process → import) per ogni entità"""
        self._run_stage(self._initial_functions, "init")

        source = self._source_fun()
        logger.info("Source fetched: %d rows", len(source))

        for process_fn, import_fn in zip(self._processing_functions,
                                         self._importing_functions):
            logger.info("Processing: %s", process_fn.__name__)
            processed = process_fn(source)

            logger.info("Importing: %s", import_fn.__name__)
            import_fn(processed)

        logger.info("Pipeline complete")


if __name__ == "__main__":
    from vab_rt_import.source import get_data
    logging.basicConfig(level=logging.INFO)
    Pipeline(source_fun=get_data).run()
