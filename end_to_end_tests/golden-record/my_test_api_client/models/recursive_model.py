from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recursive_model import RecursiveModel
else:
    RecursiveModel = "RecursiveModel"


T = TypeVar("T", bound="RecursiveModel")


@attr.s(auto_attribs=True)
class RecursiveModel:
    """ """

    recursive_model: Union[Unset, T] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        recursive_model: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recursive_model, Unset):
            recursive_model = self.recursive_model.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recursive_model is not UNSET:
            field_dict["recursive_model"] = recursive_model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _recursive_model = d.pop("recursive_model", UNSET)
        recursive_model: Union[Unset, RecursiveModel]
        if isinstance(_recursive_model, Unset):
            recursive_model = UNSET
        else:
            recursive_model = RecursiveModel.from_dict(_recursive_model)

        recursive_model = cls(
            recursive_model=recursive_model,
        )

        recursive_model.additional_properties = d
        return recursive_model

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
