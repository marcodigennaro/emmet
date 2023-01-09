from maggma.api.query_operator import PaginationQuery, SortQuery, SparseFieldsQuery
from maggma.api.resource import ReadOnlyResource

from emmet.api.core.global_header import GlobalHeaderProcessor
from emmet.api.core.settings import MAPISettings
from emmet.api.routes.materials.magnetism.query_operators import MagneticQuery
from emmet.api.routes.materials.query_operators import MultiMaterialIDQuery
from emmet.core.magnetism import MagnetismDoc


def magnetism_resource(magnetism_store):
    resource = ReadOnlyResource(
        magnetism_store,
        MagnetismDoc,
        query_operators=[
            MultiMaterialIDQuery(),
            MagneticQuery(),
            SortQuery(),
            PaginationQuery(),
            SparseFieldsQuery(MagnetismDoc, default_fields=["material_id", "last_updated"]),
        ],
        header_processor=GlobalHeaderProcessor(),
        tags=["Magnetism"],
        disable_validation=True,
        timeout=MAPISettings(DB_VERSION="").TIMEOUT,
        sub_path="/magnetism/",
    )

    return resource
