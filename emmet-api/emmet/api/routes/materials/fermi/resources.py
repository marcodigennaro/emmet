from maggma.api.query_operator import PaginationQuery, SparseFieldsQuery
from maggma.api.resource import ReadOnlyResource

from emmet.api.core.global_header import GlobalHeaderProcessor
from emmet.core.fermi import FermiDoc


def fermi_resource(fermi_store):
    resource = ReadOnlyResource(
        fermi_store,
        FermiDoc,
        query_operators=[PaginationQuery(), SparseFieldsQuery(FermiDoc, default_fields=["task_id", "last_updated"]),],
        header_processor=GlobalHeaderProcessor(),
        tags=["Electronic Structure"],
        disable_validation=True,
        sub_path="/fermi/",
    )

    return resource
