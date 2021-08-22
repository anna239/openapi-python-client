from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.circular_model_1 import CircularModel1
else:
    CircularModel1 = "CircularModel1"

from typing import Dict, Union

from ..types import UNSET, Unset

T = TypeVar("T", bound="CircularModel2")


@attr.s(auto_attribs=True)
class CircularModel2:
    """ """

    circular_model_1: Union[Unset, CircularModel1] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        circular_model_1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.circular_model_1, Unset):
            circular_model_1 = self.circular_model_1.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circular_model_1 is not UNSET:
            field_dict["circular_model_1"] = circular_model_1

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _circular_model_1 = d.pop("circular_model_1", UNSET)
        circular_model_1: Union[Unset, CircularModel1]
        if isinstance(_circular_model_1, Unset):
            circular_model_1 = UNSET
        else:
            circular_model_1 = CircularModel1.from_dict(_circular_model_1)

        circular_model_2 = cls(
            circular_model_1=circular_model_1,
        )

        circular_model_2.additional_properties = d
        return circular_model_2

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
