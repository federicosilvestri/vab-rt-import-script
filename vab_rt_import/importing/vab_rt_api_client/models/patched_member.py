from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.birth_country_enum import BirthCountryEnum
from ..models.gender_enum import GenderEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rank import Rank
    from ..models.status import Status


T = TypeVar("T", bound="PatchedMember")


@_attrs_define
class PatchedMember:
    """Full serializer for the Member model.

    - rank and status are read-only: managed internally via FSM transitions.
    - operative is read-only: computed field, not editable.
    - age is a computed property exposed as a read-only field.
    - fiscal_code is auto-filled by the model's clean() method when possible,
      so it can be left blank on creation if all birth data is provided.

        Attributes:
            id (int | Unset):
            first_name (str | Unset): Nome indicato nella carta di identità. Eventuali secondi nomi devono essere indicati
                qui, separati da uno spazio.
            last_name (str | Unset): Cognome indicato nella carta di identità. Eventuali secondi cognomi devono essere
                indicati qui, separati da uno spazio.
            gender (GenderEnum | Unset): * `M` - Maschio
                * `F` - Femmina
            citizenship (BirthCountryEnum | Unset): * `AF` - Afghanistan
                * `AX` - Åland Islands
                * `AL` - Albania
                * `DZ` - Algeria
                * `AS` - American Samoa
                * `AD` - Andorra
                * `AO` - Angola
                * `AI` - Anguilla
                * `AQ` - Antarctica
                * `AG` - Antigua and Barbuda
                * `AR` - Argentina
                * `AM` - Armenia
                * `AW` - Aruba
                * `AU` - Australia
                * `AT` - Austria
                * `AZ` - Azerbaijan
                * `BS` - Bahamas (The)
                * `BH` - Bahrain
                * `BD` - Bangladesh
                * `BB` - Barbados
                * `BY` - Belarus
                * `BE` - Belgium
                * `BZ` - Belize
                * `BJ` - Benin
                * `BM` - Bermuda
                * `BT` - Bhutan
                * `BO` - Bolivia
                * `BQ` - Bonaire, Sint Eustatius and Saba
                * `BA` - Bosnia and Herzegovina
                * `BW` - Botswana
                * `BV` - Bouvet Island
                * `BR` - Brazil
                * `IO` - British Indian Ocean Territory
                * `BN` - Brunei
                * `BG` - Bulgaria
                * `BF` - Burkina Faso
                * `BI` - Burundi
                * `CV` - Cabo Verde
                * `KH` - Cambodia
                * `CM` - Cameroon
                * `CA` - Canada
                * `KY` - Cayman Islands
                * `CF` - Central African Republic
                * `TD` - Chad
                * `CL` - Chile
                * `CN` - China
                * `CX` - Christmas Island
                * `CC` - Cocos (Keeling) Islands
                * `CO` - Colombia
                * `KM` - Comoros
                * `CG` - Congo
                * `CK` - Cook Islands
                * `CR` - Costa Rica
                * `CI` - Côte d'Ivoire
                * `HR` - Croatia
                * `CU` - Cuba
                * `CW` - Curaçao
                * `CY` - Cyprus
                * `CZ` - Czechia
                * `CD` - Democratic Republic of the Congo
                * `DK` - Denmark
                * `DJ` - Djibouti
                * `DM` - Dominica
                * `DO` - Dominican Republic
                * `EC` - Ecuador
                * `EG` - Egypt
                * `SV` - El Salvador
                * `GQ` - Equatorial Guinea
                * `ER` - Eritrea
                * `EE` - Estonia
                * `SZ` - Eswatini
                * `ET` - Ethiopia
                * `FK` - Falkland Islands (Malvinas)
                * `FO` - Faroe Islands
                * `FJ` - Fiji
                * `FI` - Finland
                * `FR` - France
                * `GF` - French Guiana
                * `PF` - French Polynesia
                * `TF` - French Southern Territories
                * `GA` - Gabon
                * `GM` - Gambia
                * `GE` - Georgia
                * `DE` - Germany
                * `GH` - Ghana
                * `GI` - Gibraltar
                * `GR` - Greece
                * `GL` - Greenland
                * `GD` - Grenada
                * `GP` - Guadeloupe
                * `GU` - Guam
                * `GT` - Guatemala
                * `GG` - Guernsey
                * `GN` - Guinea
                * `GW` - Guinea-Bissau
                * `GY` - Guyana
                * `HT` - Haiti
                * `HM` - Heard Island and McDonald Islands
                * `HN` - Honduras
                * `HK` - Hong Kong
                * `HU` - Hungary
                * `IS` - Iceland
                * `IN` - India
                * `ID` - Indonesia
                * `IR` - Iran
                * `IQ` - Iraq
                * `IE` - Ireland
                * `IM` - Isle of Man
                * `IL` - Israel
                * `IT` - Italy
                * `JM` - Jamaica
                * `JP` - Japan
                * `JE` - Jersey
                * `JO` - Jordan
                * `KZ` - Kazakhstan
                * `KE` - Kenya
                * `KI` - Kiribati
                * `KW` - Kuwait
                * `KG` - Kyrgyzstan
                * `LA` - Laos
                * `LV` - Latvia
                * `LB` - Lebanon
                * `LS` - Lesotho
                * `LR` - Liberia
                * `LY` - Libya
                * `LI` - Liechtenstein
                * `LT` - Lithuania
                * `LU` - Luxembourg
                * `MO` - Macao
                * `MG` - Madagascar
                * `MW` - Malawi
                * `MY` - Malaysia
                * `MV` - Maldives
                * `ML` - Mali
                * `MT` - Malta
                * `MH` - Marshall Islands
                * `MQ` - Martinique
                * `MR` - Mauritania
                * `MU` - Mauritius
                * `YT` - Mayotte
                * `MX` - Mexico
                * `FM` - Micronesia
                * `MD` - Moldova
                * `MC` - Monaco
                * `MN` - Mongolia
                * `ME` - Montenegro
                * `MS` - Montserrat
                * `MA` - Morocco
                * `MZ` - Mozambique
                * `MM` - Myanmar
                * `NA` - Namibia
                * `NR` - Nauru
                * `NP` - Nepal
                * `NL` - Netherlands
                * `NC` - New Caledonia
                * `NZ` - New Zealand
                * `NI` - Nicaragua
                * `NE` - Niger
                * `NG` - Nigeria
                * `NU` - Niue
                * `NF` - Norfolk Island
                * `KP` - North Korea
                * `MK` - North Macedonia
                * `MP` - Northern Mariana Islands
                * `NO` - Norway
                * `OM` - Oman
                * `PK` - Pakistan
                * `PW` - Palau
                * `PS` - Palestine
                * `PA` - Panama
                * `PG` - Papua New Guinea
                * `PY` - Paraguay
                * `PE` - Peru
                * `PH` - Philippines
                * `PN` - Pitcairn
                * `PL` - Poland
                * `PT` - Portugal
                * `PR` - Puerto Rico
                * `QA` - Qatar
                * `RE` - Réunion
                * `RO` - Romania
                * `RU` - Russia
                * `RW` - Rwanda
                * `BL` - Saint Barthélemy
                * `SH` - Saint Helena
                * `KN` - Saint Kitts and Nevis
                * `LC` - Saint Lucia
                * `MF` - Saint Martin (French part)
                * `PM` - Saint Pierre and Miquelon
                * `VC` - Saint Vincent and the Grenadines
                * `WS` - Samoa
                * `SM` - San Marino
                * `ST` - Sao Tome and Principe
                * `SA` - Saudi Arabia
                * `SN` - Senegal
                * `RS` - Serbia
                * `SC` - Seychelles
                * `SL` - Sierra Leone
                * `SG` - Singapore
                * `SX` - Sint Maarten (Dutch part)
                * `SK` - Slovakia
                * `SI` - Slovenia
                * `SB` - Solomon Islands
                * `SO` - Somalia
                * `ZA` - South Africa
                * `GS` - South Georgia
                * `KR` - South Korea
                * `SS` - South Sudan
                * `ES` - Spain
                * `LK` - Sri Lanka
                * `SD` - Sudan
                * `SR` - Suriname
                * `SJ` - Svalbard and Jan Mayen
                * `SE` - Sweden
                * `CH` - Switzerland
                * `SY` - Syria
                * `TW` - Taiwan
                * `TJ` - Tajikistan
                * `TZ` - Tanzania
                * `TH` - Thailand
                * `TL` - Timor-Leste
                * `TG` - Togo
                * `TK` - Tokelau
                * `TO` - Tonga
                * `TT` - Trinidad and Tobago
                * `TN` - Tunisia
                * `TR` - Türkiye
                * `TM` - Turkmenistan
                * `TC` - Turks and Caicos Islands
                * `TV` - Tuvalu
                * `UG` - Uganda
                * `UA` - Ukraine
                * `AE` - United Arab Emirates
                * `GB` - United Kingdom
                * `UM` - United States Minor Outlying Islands
                * `US` - United States of America
                * `UY` - Uruguay
                * `UZ` - Uzbekistan
                * `VU` - Vanuatu
                * `VA` - Vatican City
                * `VE` - Venezuela
                * `VN` - Vietnam
                * `VG` - Virgin Islands (British)
                * `VI` - Virgin Islands (U.S.)
                * `WF` - Wallis and Futuna
                * `EH` - Western Sahara
                * `YE` - Yemen
                * `ZM` - Zambia
                * `ZW` - Zimbabwe
            birth_date (datetime.date | Unset): Data di nascita
            birth_country (BirthCountryEnum | Unset): * `AF` - Afghanistan
                * `AX` - Åland Islands
                * `AL` - Albania
                * `DZ` - Algeria
                * `AS` - American Samoa
                * `AD` - Andorra
                * `AO` - Angola
                * `AI` - Anguilla
                * `AQ` - Antarctica
                * `AG` - Antigua and Barbuda
                * `AR` - Argentina
                * `AM` - Armenia
                * `AW` - Aruba
                * `AU` - Australia
                * `AT` - Austria
                * `AZ` - Azerbaijan
                * `BS` - Bahamas (The)
                * `BH` - Bahrain
                * `BD` - Bangladesh
                * `BB` - Barbados
                * `BY` - Belarus
                * `BE` - Belgium
                * `BZ` - Belize
                * `BJ` - Benin
                * `BM` - Bermuda
                * `BT` - Bhutan
                * `BO` - Bolivia
                * `BQ` - Bonaire, Sint Eustatius and Saba
                * `BA` - Bosnia and Herzegovina
                * `BW` - Botswana
                * `BV` - Bouvet Island
                * `BR` - Brazil
                * `IO` - British Indian Ocean Territory
                * `BN` - Brunei
                * `BG` - Bulgaria
                * `BF` - Burkina Faso
                * `BI` - Burundi
                * `CV` - Cabo Verde
                * `KH` - Cambodia
                * `CM` - Cameroon
                * `CA` - Canada
                * `KY` - Cayman Islands
                * `CF` - Central African Republic
                * `TD` - Chad
                * `CL` - Chile
                * `CN` - China
                * `CX` - Christmas Island
                * `CC` - Cocos (Keeling) Islands
                * `CO` - Colombia
                * `KM` - Comoros
                * `CG` - Congo
                * `CK` - Cook Islands
                * `CR` - Costa Rica
                * `CI` - Côte d'Ivoire
                * `HR` - Croatia
                * `CU` - Cuba
                * `CW` - Curaçao
                * `CY` - Cyprus
                * `CZ` - Czechia
                * `CD` - Democratic Republic of the Congo
                * `DK` - Denmark
                * `DJ` - Djibouti
                * `DM` - Dominica
                * `DO` - Dominican Republic
                * `EC` - Ecuador
                * `EG` - Egypt
                * `SV` - El Salvador
                * `GQ` - Equatorial Guinea
                * `ER` - Eritrea
                * `EE` - Estonia
                * `SZ` - Eswatini
                * `ET` - Ethiopia
                * `FK` - Falkland Islands (Malvinas)
                * `FO` - Faroe Islands
                * `FJ` - Fiji
                * `FI` - Finland
                * `FR` - France
                * `GF` - French Guiana
                * `PF` - French Polynesia
                * `TF` - French Southern Territories
                * `GA` - Gabon
                * `GM` - Gambia
                * `GE` - Georgia
                * `DE` - Germany
                * `GH` - Ghana
                * `GI` - Gibraltar
                * `GR` - Greece
                * `GL` - Greenland
                * `GD` - Grenada
                * `GP` - Guadeloupe
                * `GU` - Guam
                * `GT` - Guatemala
                * `GG` - Guernsey
                * `GN` - Guinea
                * `GW` - Guinea-Bissau
                * `GY` - Guyana
                * `HT` - Haiti
                * `HM` - Heard Island and McDonald Islands
                * `HN` - Honduras
                * `HK` - Hong Kong
                * `HU` - Hungary
                * `IS` - Iceland
                * `IN` - India
                * `ID` - Indonesia
                * `IR` - Iran
                * `IQ` - Iraq
                * `IE` - Ireland
                * `IM` - Isle of Man
                * `IL` - Israel
                * `IT` - Italy
                * `JM` - Jamaica
                * `JP` - Japan
                * `JE` - Jersey
                * `JO` - Jordan
                * `KZ` - Kazakhstan
                * `KE` - Kenya
                * `KI` - Kiribati
                * `KW` - Kuwait
                * `KG` - Kyrgyzstan
                * `LA` - Laos
                * `LV` - Latvia
                * `LB` - Lebanon
                * `LS` - Lesotho
                * `LR` - Liberia
                * `LY` - Libya
                * `LI` - Liechtenstein
                * `LT` - Lithuania
                * `LU` - Luxembourg
                * `MO` - Macao
                * `MG` - Madagascar
                * `MW` - Malawi
                * `MY` - Malaysia
                * `MV` - Maldives
                * `ML` - Mali
                * `MT` - Malta
                * `MH` - Marshall Islands
                * `MQ` - Martinique
                * `MR` - Mauritania
                * `MU` - Mauritius
                * `YT` - Mayotte
                * `MX` - Mexico
                * `FM` - Micronesia
                * `MD` - Moldova
                * `MC` - Monaco
                * `MN` - Mongolia
                * `ME` - Montenegro
                * `MS` - Montserrat
                * `MA` - Morocco
                * `MZ` - Mozambique
                * `MM` - Myanmar
                * `NA` - Namibia
                * `NR` - Nauru
                * `NP` - Nepal
                * `NL` - Netherlands
                * `NC` - New Caledonia
                * `NZ` - New Zealand
                * `NI` - Nicaragua
                * `NE` - Niger
                * `NG` - Nigeria
                * `NU` - Niue
                * `NF` - Norfolk Island
                * `KP` - North Korea
                * `MK` - North Macedonia
                * `MP` - Northern Mariana Islands
                * `NO` - Norway
                * `OM` - Oman
                * `PK` - Pakistan
                * `PW` - Palau
                * `PS` - Palestine
                * `PA` - Panama
                * `PG` - Papua New Guinea
                * `PY` - Paraguay
                * `PE` - Peru
                * `PH` - Philippines
                * `PN` - Pitcairn
                * `PL` - Poland
                * `PT` - Portugal
                * `PR` - Puerto Rico
                * `QA` - Qatar
                * `RE` - Réunion
                * `RO` - Romania
                * `RU` - Russia
                * `RW` - Rwanda
                * `BL` - Saint Barthélemy
                * `SH` - Saint Helena
                * `KN` - Saint Kitts and Nevis
                * `LC` - Saint Lucia
                * `MF` - Saint Martin (French part)
                * `PM` - Saint Pierre and Miquelon
                * `VC` - Saint Vincent and the Grenadines
                * `WS` - Samoa
                * `SM` - San Marino
                * `ST` - Sao Tome and Principe
                * `SA` - Saudi Arabia
                * `SN` - Senegal
                * `RS` - Serbia
                * `SC` - Seychelles
                * `SL` - Sierra Leone
                * `SG` - Singapore
                * `SX` - Sint Maarten (Dutch part)
                * `SK` - Slovakia
                * `SI` - Slovenia
                * `SB` - Solomon Islands
                * `SO` - Somalia
                * `ZA` - South Africa
                * `GS` - South Georgia
                * `KR` - South Korea
                * `SS` - South Sudan
                * `ES` - Spain
                * `LK` - Sri Lanka
                * `SD` - Sudan
                * `SR` - Suriname
                * `SJ` - Svalbard and Jan Mayen
                * `SE` - Sweden
                * `CH` - Switzerland
                * `SY` - Syria
                * `TW` - Taiwan
                * `TJ` - Tajikistan
                * `TZ` - Tanzania
                * `TH` - Thailand
                * `TL` - Timor-Leste
                * `TG` - Togo
                * `TK` - Tokelau
                * `TO` - Tonga
                * `TT` - Trinidad and Tobago
                * `TN` - Tunisia
                * `TR` - Türkiye
                * `TM` - Turkmenistan
                * `TC` - Turks and Caicos Islands
                * `TV` - Tuvalu
                * `UG` - Uganda
                * `UA` - Ukraine
                * `AE` - United Arab Emirates
                * `GB` - United Kingdom
                * `UM` - United States Minor Outlying Islands
                * `US` - United States of America
                * `UY` - Uruguay
                * `UZ` - Uzbekistan
                * `VU` - Vanuatu
                * `VA` - Vatican City
                * `VE` - Venezuela
                * `VN` - Vietnam
                * `VG` - Virgin Islands (British)
                * `VI` - Virgin Islands (U.S.)
                * `WF` - Wallis and Futuna
                * `EH` - Western Sahara
                * `YE` - Yemen
                * `ZM` - Zambia
                * `ZW` - Zimbabwe
            birth_comune (int | None | Unset):
            fiscal_code (str | Unset):
            socio (bool | None | Unset):
            volontario (bool | None | Unset):
            rank (None | Rank | Unset):
            status (None | Status | Unset):
            operative (bool | Unset): Indica se la persona è operativa.
            age (None | str | Unset):
    """

    id: int | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    gender: GenderEnum | Unset = UNSET
    citizenship: BirthCountryEnum | Unset = UNSET
    birth_date: datetime.date | Unset = UNSET
    birth_country: BirthCountryEnum | Unset = UNSET
    birth_comune: int | None | Unset = UNSET
    fiscal_code: str | Unset = UNSET
    socio: bool | None | Unset = UNSET
    volontario: bool | None | Unset = UNSET
    rank: None | Rank | Unset = UNSET
    status: None | Status | Unset = UNSET
    operative: bool | Unset = UNSET
    age: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rank import Rank
        from ..models.status import Status

        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        gender: str | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        citizenship: str | Unset = UNSET
        if not isinstance(self.citizenship, Unset):
            citizenship = self.citizenship.value

        birth_date: str | Unset = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.strftime('%Y-%m-%d')

        birth_country: str | Unset = UNSET
        if not isinstance(self.birth_country, Unset):
            birth_country = self.birth_country.value

        birth_comune: int | None | Unset
        if isinstance(self.birth_comune, Unset):
            birth_comune = UNSET
        else:
            birth_comune = self.birth_comune

        fiscal_code = self.fiscal_code

        socio: bool | None | Unset
        if isinstance(self.socio, Unset):
            socio = UNSET
        else:
            socio = self.socio

        volontario: bool | None | Unset
        if isinstance(self.volontario, Unset):
            volontario = UNSET
        else:
            volontario = self.volontario

        rank: dict[str, Any] | None | Unset
        if isinstance(self.rank, Unset):
            rank = UNSET
        elif isinstance(self.rank, Rank):
            rank = self.rank.to_dict()
        else:
            rank = self.rank

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, Status):
            status = self.status.to_dict()
        else:
            status = self.status

        operative = self.operative

        age: None | str | Unset
        if isinstance(self.age, Unset):
            age = UNSET
        else:
            age = self.age

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if citizenship is not UNSET:
            field_dict["citizenship"] = citizenship
        if birth_date is not UNSET:
            field_dict["birth_date"] = birth_date
        if birth_country is not UNSET:
            field_dict["birth_country"] = birth_country
        if birth_comune is not UNSET:
            field_dict["birth_comune"] = birth_comune
        if fiscal_code is not UNSET:
            field_dict["fiscal_code"] = fiscal_code
        if socio is not UNSET:
            field_dict["socio"] = socio
        if volontario is not UNSET:
            field_dict["volontario"] = volontario
        if rank is not UNSET:
            field_dict["rank"] = rank
        if status is not UNSET:
            field_dict["status"] = status
        if operative is not UNSET:
            field_dict["operative"] = operative
        if age is not UNSET:
            field_dict["age"] = age

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rank import Rank
        from ..models.status import Status

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: GenderEnum | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = GenderEnum(_gender)

        _citizenship = d.pop("citizenship", UNSET)
        citizenship: BirthCountryEnum | Unset
        if isinstance(_citizenship, Unset):
            citizenship = UNSET
        else:
            citizenship = BirthCountryEnum(_citizenship)

        _birth_date = d.pop("birth_date", UNSET)
        birth_date: datetime.date | Unset
        if isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = isoparse(_birth_date).date()

        _birth_country = d.pop("birth_country", UNSET)
        birth_country: BirthCountryEnum | Unset
        if isinstance(_birth_country, Unset):
            birth_country = UNSET
        else:
            birth_country = BirthCountryEnum(_birth_country)

        def _parse_birth_comune(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        birth_comune = _parse_birth_comune(d.pop("birth_comune", UNSET))

        fiscal_code = d.pop("fiscal_code", UNSET)

        def _parse_socio(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        socio = _parse_socio(d.pop("socio", UNSET))

        def _parse_volontario(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        volontario = _parse_volontario(d.pop("volontario", UNSET))

        def _parse_rank(data: object) -> None | Rank | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rank_type_1 = Rank.from_dict(data)

                return rank_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Rank | Unset, data)

        rank = _parse_rank(d.pop("rank", UNSET))

        def _parse_status(data: object) -> None | Status | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = Status.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Status | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        operative = d.pop("operative", UNSET)

        def _parse_age(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        age = _parse_age(d.pop("age", UNSET))

        patched_member = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            citizenship=citizenship,
            birth_date=birth_date,
            birth_country=birth_country,
            birth_comune=birth_comune,
            fiscal_code=fiscal_code,
            socio=socio,
            volontario=volontario,
            rank=rank,
            status=status,
            operative=operative,
            age=age,
        )

        patched_member.additional_properties = d
        return patched_member

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
