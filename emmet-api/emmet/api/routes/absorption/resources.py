from maggma.api.resource import ReadOnlyResource

from maggma.api.query_operator import PaginationQuery, SortQuery, SparseFieldsQuery

from emmet.core.absorption import AbsorptionDoc

from emmet.api.core.settings import MAPISettings
from emmet.api.routes.materials.query_operators import (
    ElementsQuery,
    FormulaQuery,
    ChemsysQuery,
    MultiMaterialIDQuery,
)


def absorption_pairs_resource(absorption_pairs_store):
    resource = ReadOnlyResource(
        absorption_pairs_store,
        AbsorptionDoc,
        query_operators=[
            MultiMaterialIDQuery(),
            FormulaQuery(),
            ElementsQuery(),
            ChemsysQuery(),
            SortQuery(),
            PaginationQuery(),
            SparseFieldsQuery(AbsorptionDoc, default_fields=["material_id"],),
        ],
        tags=["Absorption"],
        disable_validation=True,
        timeout=MAPISettings().TIMEOUT,
    )

    return resource
