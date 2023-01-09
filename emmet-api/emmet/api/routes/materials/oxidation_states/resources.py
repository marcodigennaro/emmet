from maggma.api.query_operator import PaginationQuery, SortQuery, SparseFieldsQuery
from maggma.api.resource import ReadOnlyResource

from emmet.api.core.global_header import GlobalHeaderProcessor
from emmet.api.core.settings import MAPISettings
from emmet.api.routes.materials.oxidation_states.query_operators import PossibleOxiStateQuery
from emmet.api.routes.materials.query_operators import (
    ChemsysQuery,
    FormulaQuery,
    MultiMaterialIDQuery,
)
from emmet.core.oxidation_states import OxidationStateDoc


def oxi_states_resource(oxi_states_store):
    resource = ReadOnlyResource(
        oxi_states_store,
        OxidationStateDoc,
        query_operators=[
            MultiMaterialIDQuery(),
            FormulaQuery(),
            ChemsysQuery(),
            PossibleOxiStateQuery(),
            SortQuery(),
            PaginationQuery(),
            SparseFieldsQuery(OxidationStateDoc, default_fields=["material_id", "last_updated"]),
        ],
        header_processor=GlobalHeaderProcessor(),
        tags=["Oxidation States"],
        disable_validation=True,
        timeout=MAPISettings().TIMEOUT,
        sub_path="/oxidation_states/",
    )

    return resource
