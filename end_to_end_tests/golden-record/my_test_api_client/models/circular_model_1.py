from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.circular_model_2 import CircularModel2
else:
    CircularModel2 = "CircularModel2"

from typing import Dict, Union

T = TypeVar("T", bound="CircularModel1")


@attr.s(auto_attribs=True)
class CircularModel1:
    """ """

    circular_model_2: Union[Unset, CircularModel2] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        circular_model_2: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.circular_model_2, Unset):
            circular_model_2 = self.circular_model_2.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circular_model_2 is not UNSET:
            field_dict["circular_model_2"] = circular_model_2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _circular_model_2 = d.pop("circular_model_2", UNSET)
        circular_model_2: Union[Unset, CircularModel2]
        if isinstance(_circular_model_2, Unset):
            circular_model_2 = UNSET
        else:
            circular_model_2 = CircularModel2.from_dict(_circular_model_2)

        circular_model_1 = cls(
            circular_model_2=circular_model_2,
        )

        circular_model_1.additional_properties = d
        return circular_model_1

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
