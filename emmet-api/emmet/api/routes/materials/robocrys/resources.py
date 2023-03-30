from maggma.api.query_operator import PaginationQuery, SparseFieldsQuery
from maggma.api.resource import ReadOnlyResource
from maggma.api.resource.aggregation import AggregationResource

from emmet.api.core.global_header import GlobalHeaderProcessor
from emmet.api.core.settings import MAPISettings
from emmet.api.routes.materials.query_operators import MultiMaterialIDQuery
from emmet.api.routes.materials.robocrys.query_operators import RoboTextSearchQuery
from emmet.core.robocrys import RobocrystallogapherDoc

timeout = MAPISettings(DB_VERSION="").TIMEOUT


def robo_resource(robo_store):
    resource = ReadOnlyResource(
        robo_store,
        RobocrystallogapherDoc,
        query_operators=[
            MultiMaterialIDQuery(),
            PaginationQuery(),
            SparseFieldsQuery(
                RobocrystallogapherDoc, default_fields=["material_id", "last_updated"]
            ),
        ],
        header_processor=GlobalHeaderProcessor(),
        tags=["Robocrystallographer"],
        disable_validation=True,
        timeout=timeout,
        sub_path="/robocrys/",
    )

    return resource


def robo_search_resource(robo_store):
    resource = AggregationResource(
        robo_store,
        RobocrystallogapherDoc,
        pipeline_query_operator=RoboTextSearchQuery(),
        tags=["Robocrystallographer"],
        header_processor=GlobalHeaderProcessor(),
        timeout=timeout,
        sub_path="/robocrys/text_search/",
    )

    return resource
