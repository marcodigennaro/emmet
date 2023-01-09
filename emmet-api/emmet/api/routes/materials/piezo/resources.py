from maggma.api.query_operator import PaginationQuery, SortQuery, SparseFieldsQuery
from maggma.api.resource import ReadOnlyResource

from emmet.api.core.global_header import GlobalHeaderProcessor
from emmet.api.core.settings import MAPISettings
from emmet.api.routes.materials.piezo.query_operators import PiezoelectricQuery
from emmet.api.routes.materials.query_operators import MultiMaterialIDQuery
from emmet.core.polar import PiezoelectricDoc


def piezo_resource(piezo_store):
    resource = ReadOnlyResource(
        piezo_store,
        PiezoelectricDoc,
        query_operators=[
            MultiMaterialIDQuery(),
            PiezoelectricQuery(),
            SortQuery(),
            PaginationQuery(),
            SparseFieldsQuery(PiezoelectricDoc, default_fields=["material_id", "last_updated"]),
        ],
        header_processor=GlobalHeaderProcessor(),
        tags=["Piezoelectric"],
        disable_validation=True,
        timeout=MAPISettings().TIMEOUT,
        sub_path="/piezoelectric/",
    )

    return resource
