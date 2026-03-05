from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.birth_country_enum import BirthCountryEnum
from ..models.education_type_enum import EducationTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedMemberEducation")


@_attrs_define
class PatchedMemberEducation:
    """Serializer for MemberEducation.

    Specialization is required for university-level education types.
    The model's clean() validates this constraint.

        Attributes:
            id (int | Unset):
            member (int | Unset):
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
            education_type (EducationTypeEnum | Unset): * `TERZA_MEDIA` - Diploma Terza Media
                * `SCUOLA_SUPERIORE` - Diploma Scuola Superiore
                * `LAUREA_TRIENNALE` - Laurea Triennale
                * `LAUREA_MAGISTRALE` - Laurea Magistrale
                * `LAUREA_CICLO_UNICO` - Laurea Ciclo Unico
                * `LAUREA_VECCHIO_ORDINAMENTO` - Laurea Vecchio Ordinamento
                * `DOTTORATO` - Dottorato di Ricerca
                * `MASTER_I_LIV` - Master Universitario I livello
                * `MASTER_II_LIV` - Master Universitario II livello
                * `MASTER_ALTRI` - Master / corso post-laurea non universitario
            name (str | Unset): Nome della scuola/istituto/università
            program_name (str | Unset): Programma della scuola/istituto o nome della facoltà
            specialization (str | Unset): Indirizzo, major o facoltà, se applicabile
            end_date (datetime.date | Unset): Indicare la data di conseguimento del titolo.
            notes (str | Unset): Eventuali note.
    """

    id: int | Unset = UNSET
    member: int | Unset = UNSET
    country: BirthCountryEnum | Unset = UNSET
    education_type: EducationTypeEnum | Unset = UNSET
    name: str | Unset = UNSET
    program_name: str | Unset = UNSET
    specialization: str | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        country: str | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        education_type: str | Unset = UNSET
        if not isinstance(self.education_type, Unset):
            education_type = self.education_type.value

        name = self.name

        program_name = self.program_name

        specialization = self.specialization

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.strftime('%Y-%m-%d')

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if member is not UNSET:
            field_dict["member"] = member
        if country is not UNSET:
            field_dict["country"] = country
        if education_type is not UNSET:
            field_dict["education_type"] = education_type
        if name is not UNSET:
            field_dict["name"] = name
        if program_name is not UNSET:
            field_dict["program_name"] = program_name
        if specialization is not UNSET:
            field_dict["specialization"] = specialization
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        member = d.pop("member", UNSET)

        _country = d.pop("country", UNSET)
        country: BirthCountryEnum | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = BirthCountryEnum(_country)

        _education_type = d.pop("education_type", UNSET)
        education_type: EducationTypeEnum | Unset
        if isinstance(_education_type, Unset):
            education_type = UNSET
        else:
            education_type = EducationTypeEnum(_education_type)

        name = d.pop("name", UNSET)

        program_name = d.pop("program_name", UNSET)

        specialization = d.pop("specialization", UNSET)

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        notes = d.pop("notes", UNSET)

        patched_member_education = cls(
            id=id,
            member=member,
            country=country,
            education_type=education_type,
            name=name,
            program_name=program_name,
            specialization=specialization,
            end_date=end_date,
            notes=notes,
        )

        patched_member_education.additional_properties = d
        return patched_member_education

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
