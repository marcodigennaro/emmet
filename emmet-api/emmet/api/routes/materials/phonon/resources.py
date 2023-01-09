from maggma.api.query_operator import PaginationQuery, SparseFieldsQuery
from maggma.api.resource import ReadOnlyResource

from emmet.api.core.global_header import GlobalHeaderProcessor
from emmet.api.core.settings import MAPISettings
from emmet.core.phonon import PhononBSDOSDoc


def phonon_bsdos_resource(phonon_bs_store):
    resource = ReadOnlyResource(
        phonon_bs_store,
        PhononBSDOSDoc,
        query_operators=[
            PaginationQuery(),
            SparseFieldsQuery(PhononBSDOSDoc, default_fields=["task_id", "last_updated"]),
        ],
        header_processor=GlobalHeaderProcessor(),
        tags=["Phonon"],
        enable_default_search=False,
        disable_validation=True,
        timeout=MAPISettings(DB_VERSION="").TIMEOUT,
        sub_path="/phonon/",
    )

    return resource
