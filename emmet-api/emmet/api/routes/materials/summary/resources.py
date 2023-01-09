from maggma.api.query_operator import (
    NumericQuery,
    PaginationQuery,
    SortQuery,
    SparseFieldsQuery,
)
from maggma.api.resource import AggregationResource, ReadOnlyResource

from emmet.api.core.global_header import GlobalHeaderProcessor
from emmet.api.core.settings import MAPISettings
from emmet.api.routes.materials.oxidation_states.query_operators import PossibleOxiStateQuery
from emmet.api.routes.materials.query_operators import (
    ChemsysQuery,
    DeprecationQuery,
    ElementsQuery,
    FormulaQuery,
    SymmetryQuery,
)
from emmet.api.routes.materials.summary.hint_scheme import SummaryHintScheme
from emmet.api.routes.materials.summary.query_operators import (
    HasPropsQuery,
    MaterialIDsSearchQuery,
    SearchESQuery,
    SearchHasReconstructedQuery,
    SearchIsStableQuery,
    SearchIsTheoreticalQuery,
    SearchMagneticQuery,
    SearchStatsQuery,
)
from emmet.core.summary import SummaryDoc, SummaryStats

timeout = MAPISettings(DB_VERSION="").TIMEOUT


def summary_resource(summary_store):
    resource = ReadOnlyResource(
        summary_store,
        SummaryDoc,
        query_operators=[
            MaterialIDsSearchQuery(),
            FormulaQuery(),
            ChemsysQuery(),
            ElementsQuery(),
            PossibleOxiStateQuery(),
            SymmetryQuery(),
            SearchIsStableQuery(),
            SearchIsTheoreticalQuery(),
            SearchMagneticQuery(),
            SearchESQuery(),
            NumericQuery(model=SummaryDoc, excluded_fields=["composition"]),
            SearchHasReconstructedQuery(),
            HasPropsQuery(),
            DeprecationQuery(),
            SortQuery(),
            PaginationQuery(),
            SparseFieldsQuery(SummaryDoc, default_fields=["material_id"]),
        ],
        hint_scheme=SummaryHintScheme(),
        header_processor=GlobalHeaderProcessor(),
        tags=["Summary"],
        disable_validation=True,
        timeout=timeout,
        sub_path="/summary/",
    )

    return resource


def summary_stats_resource(summary_store):
    resource = AggregationResource(
        summary_store,
        SummaryStats,
        pipeline_query_operator=SearchStatsQuery(SummaryDoc),
        tags=["Summary"],
        header_processor=GlobalHeaderProcessor(),
        timeout=timeout,
        sub_path="/summary/stats/",
    )

    return resource
