from maggma.api.query_operator import (
    NumericQuery,
    PaginationQuery,
    SortQuery,
    SparseFieldsQuery,
    StringQueryOperator,
)
from maggma.api.resource import ReadOnlyResource

from emmet.api.core.global_header import GlobalHeaderProcessor
from emmet.api.core.settings import MAPISettings
from emmet.api.routes.materials.substrates.query_operators import SubstrateStructureQuery
from emmet.core.substrates import SubstratesDoc


def substrates_resource(substrates_store):
    resource = ReadOnlyResource(
        substrates_store,
        SubstratesDoc,
        query_operators=[
            SubstrateStructureQuery(),
            NumericQuery(model=SubstratesDoc),
            StringQueryOperator(model=SubstratesDoc, excluded_fields=["film_orient", "orient"]),
            SortQuery(),
            PaginationQuery(),
            SparseFieldsQuery(SubstratesDoc, default_fields=["film_id", "sub_id"]),
        ],
        header_processor=GlobalHeaderProcessor(),
        tags=["Substrates"],
        enable_get_by_key=False,
        disable_validation=True,
        timeout=MAPISettings(DB_VERSION="").TIMEOUT,
        sub_path="/substrates/",
    )

    return resource
