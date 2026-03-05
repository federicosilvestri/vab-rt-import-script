from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.birth_country_enum import BirthCountryEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberAddress")


@_attrs_define
class MemberAddress:
    """Serializer for MemberAddress.

    Italian addresses require region/province/comune/postal_code/street/street_number.
    Foreign addresses only require country + foreign_address.
    The model's clean() method handles autofill and cross-field validation.

    The 'point' (geospatial) field is intentionally excluded: it is auto-computed
    and not meant to be set or displayed directly via the API.

        Attributes:
            id (int):
            member (int):
            country (BirthCountryEnum | Unset): * `AF` - Afghanistan
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
            foreign_address (str | Unset): Indirizzo estero, da compilare solo in cui la nazione non sia italiana.
            region (int | None | Unset):
            province (int | None | Unset):
            comune (int | None | Unset): Comune di residenza/domicilio
            postal_code (str | Unset):
            street (str | Unset):
            street_number (str | Unset):
            residence (bool | Unset): Indicare se questo è un indirizzo di residenza, altrimenti sarà considerato come
                domicilio.
    """

    id: int
    member: int
    country: BirthCountryEnum | Unset = UNSET
    foreign_address: str | Unset = UNSET
    region: int | None | Unset = UNSET
    province: int | None | Unset = UNSET
    comune: int | None | Unset = UNSET
    postal_code: str | Unset = UNSET
    street: str | Unset = UNSET
    street_number: str | Unset = UNSET
    residence: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        country: str | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        foreign_address = self.foreign_address

        region: int | None | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        province: int | None | Unset
        if isinstance(self.province, Unset):
            province = UNSET
        else:
            province = self.province

        comune: int | None | Unset
        if isinstance(self.comune, Unset):
            comune = UNSET
        else:
            comune = self.comune

        postal_code = self.postal_code

        street = self.street

        street_number = self.street_number

        residence = self.residence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member": member,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country
        if foreign_address is not UNSET:
            field_dict["foreign_address"] = foreign_address
        if region is not UNSET:
            field_dict["region"] = region
        if province is not UNSET:
            field_dict["province"] = province
        if comune is not UNSET:
            field_dict["comune"] = comune
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if street is not UNSET:
            field_dict["street"] = street
        if street_number is not UNSET:
            field_dict["street_number"] = street_number
        if residence is not UNSET:
            field_dict["residence"] = residence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        member = d.pop("member")

        _country = d.pop("country", UNSET)
        country: BirthCountryEnum | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = BirthCountryEnum(_country)

        foreign_address = d.pop("foreign_address", UNSET)

        def _parse_region(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_province(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        province = _parse_province(d.pop("province", UNSET))

        def _parse_comune(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        comune = _parse_comune(d.pop("comune", UNSET))

        postal_code = d.pop("postal_code", UNSET)

        street = d.pop("street", UNSET)

        street_number = d.pop("street_number", UNSET)

        residence = d.pop("residence", UNSET)

        member_address = cls(
            id=id,
            member=member,
            country=country,
            foreign_address=foreign_address,
            region=region,
            province=province,
            comune=comune,
            postal_code=postal_code,
            street=street,
            street_number=street_number,
            residence=residence,
        )

        member_address.additional_properties = d
        return member_address

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
