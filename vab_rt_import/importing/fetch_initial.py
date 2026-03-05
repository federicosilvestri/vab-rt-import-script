"""Fetch initial data before importing"""
import logging

from .utils.geo_map import GeoLookup


def main():
    """Main function"""
    logging.basicConfig(level=logging.INFO)
    GeoLookup()

if __name__ == "__main__":
    main()