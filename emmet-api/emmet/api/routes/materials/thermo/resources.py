from maggma.api.query_operator import PaginationQuery, SortQuery, SparseFieldsQuery
from maggma.api.query_operator.dynamic import NumericQuery
from maggma.api.resource import ReadOnlyResource

from emmet.api.core.global_header import GlobalHeaderProcessor
from emmet.api.core.settings import MAPISettings
from emmet.api.routes.materials.query_operators import (
    ChemsysQuery,
    FormulaQuery,
    MultiMaterialIDQuery,
)
from emmet.api.routes.materials.thermo.query_operators import (
    IsStableQuery,
    MultiThermoIDQuery,
    MultiThermoTypeQuery,
)
from emmet.core.thermo import PhaseDiagramDoc, ThermoDoc


def phase_diagram_resource(phase_diagram_store):
    resource = ReadOnlyResource(
        phase_diagram_store,
        PhaseDiagramDoc,
        tags=["Thermo"],
        disable_validation=True,
        enable_default_search=False,
        header_processor=GlobalHeaderProcessor(),
        query_disk_use=False,
        sub_path="/thermo/phase_diagram/",
    )

    return resource


def thermo_resource(thermo_store):
    resource = ReadOnlyResource(
        thermo_store,
        ThermoDoc,
        query_operators=[
            MultiThermoIDQuery(),
            MultiMaterialIDQuery(),
            MultiThermoTypeQuery(),
            FormulaQuery(),
            ChemsysQuery(),
            IsStableQuery(),
            NumericQuery(model=ThermoDoc),
            SortQuery(),
            PaginationQuery(),
            SparseFieldsQuery(ThermoDoc, default_fields=["thermo_id", "material_id", "last_updated"]),
        ],
        header_processor=GlobalHeaderProcessor(),
        tags=["Thermo"],
        disable_validation=True,
        timeout=MAPISettings(DB_VERSION="").TIMEOUT,
        sub_path="/thermo/",
    )

    return resource
