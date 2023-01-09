import os

from emmet.api.core.api import MAPI
from emmet.api.core.settings import MAPISettings
from maggma.stores import MongoURIStore, S3Store

resources = {}

default_settings = MAPISettings()

db_uri = os.environ.get("MPCONTRIBS_MONGO_HOST", None)
db_version = default_settings.DB_VERSION
db_suffix = os.environ["MAPI_DB_NAME_SUFFIX"]
debug = default_settings.DEBUG

# allow db_uri to be set with a different protocol scheme
# but prepend with mongodb+srv:// if not otherwise specified
if len(db_uri.split("://", 1)) < 2:
    db_uri = "mongodb+srv://" + db_uri

if db_uri:

    materials_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="material_id", collection_name="materials",
    )

    bonds_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="material_id", collection_name="bonds",
    )

    formula_autocomplete_store = MongoURIStore(
        uri=db_uri, database="mp_core", key="_id", collection_name="formula_autocomplete",
    )

    task_store = MongoURIStore(uri=db_uri, database="mp_core", key="task_id", collection_name="tasks",)

    thermo_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="thermo_id", collection_name="thermo",
    )

    s3_phase_diagram_index = MongoURIStore(
        uri=db_uri, database="mp_core", key="phase_diagram_id", collection_name="s3_phase_diagram_index",
    )

    phase_diagram_store = S3Store(
        index=s3_phase_diagram_index,
        bucket="mp-phase-diagrams",
        s3_workers=24,
        key="phase_diagram_id",
        searchable_fields=["chemsys", "thermo_type", "phase_diagram_id"],
        compress=True,
    )

    dielectric_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="material_id", collection_name="dielectric",
    )

    piezoelectric_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="material_id", collection_name="piezoelectric",
    )

    magnetism_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="material_id", collection_name="magnetism",
    )

    phonon_bs_store = MongoURIStore(uri=db_uri, database="mp_core", key="material_id", collection_name="pmg_ph_bs",)

    eos_store = MongoURIStore(uri=db_uri, database="mp_core", key="task_id", collection_name="eos",)

    similarity_store = MongoURIStore(uri=db_uri, database="mp_core", key="material_id", collection_name="similarity",)

    xas_store = MongoURIStore(uri=db_uri, database="mp_core", key="spectrum_id", collection_name="xas",)

    gb_store = MongoURIStore(uri=db_uri, database="mp_core", key="task_id", collection_name="grain_boundaries",)

    fermi_store = MongoURIStore(uri=db_uri, database="mp_core", key="task_id", collection_name="fermi_surface",)

    elasticity_store = MongoURIStore(uri=db_uri, database="mp_core", key="task_id", collection_name="elasticity",)

    doi_store = MongoURIStore(uri=db_uri, database="mp_core", key="task_id", collection_name="dois",)

    substrates_store = MongoURIStore(uri=db_uri, database="mp_core", key="film_id", collection_name="substrates",)

    surface_props_store = MongoURIStore(
        uri=db_uri, database="mp_core", key="task_id", collection_name="surface_properties",
    )

    robo_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="material_id", collection_name="robocrys",
    )

    synth_store = MongoURIStore(uri=db_uri, database="mp_core", key="_id", collection_name="synth_descriptions",)

    insertion_electrodes_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="battery_id", collection_name="insertion_electrodes",
    )

    molecules_store = MongoURIStore(uri=db_uri, database="mp_core", key="task_id", collection_name="molecules",)

    oxi_states_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="material_id", collection_name="oxi_states",
    )

    provenance_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="material_id", collection_name="provenance",
    )

    alloy_pairs_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="pair_id", collection_name="alloy_pairs",
    )

    summary_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="material_id", collection_name="summary",
    )

    es_store = MongoURIStore(
        uri=db_uri, database=f"mp_core_{db_suffix}", key="material_id", collection_name="electronic_structure",
    )

    s3_bs_index = MongoURIStore(uri=db_uri, database="mp_core", key="fs_id", collection_name="s3_bandstructure_index",)

    s3_dos_index = MongoURIStore(uri=db_uri, database="mp_core", key="fs_id", collection_name="s3_dos_index",)

    s3_bs = S3Store(
        index=s3_bs_index,
        bucket="mp-bandstructures",
        compress=True,
        key="fs_id",
        unpack_data=False,
        searchable_fields=["task_id", "fs_id"],
    )

    s3_dos = S3Store(
        index=s3_dos_index,
        bucket="mp-dos",
        compress=True,
        key="fs_id",
        unpack_data=False,
        searchable_fields=["task_id", "fs_id"],
    )

    s3_chgcar_index = MongoURIStore(
        uri=db_uri, database="mp_core", key="fs_id", collection_name="atomate_chgcar_fs_index",
    )

    s3_chgcar = S3Store(
        index=s3_chgcar_index,
        bucket="mp-volumetric",
        sub_dir="atomate_chgcar_fs/",
        compress=True,
        key="fs_id",
        unpack_data=False,
        searchable_fields=["task_id", "fs_id"],
    )

    chgcar_url = MongoURIStore(uri=db_uri, database="mp_core", key="fs_id", collection_name="chgcar_s3_urls",)

    mpcomplete_store = MongoURIStore(
        uri=db_uri, database="mp_consumers", key="submission_id", collection_name="mpcomplete",
    )

    consumer_settings_store = MongoURIStore(
        uri=db_uri, database="mp_consumers", key="consumer_id", collection_name="settings",
    )

    general_store = MongoURIStore(
        uri=db_uri, database="mp_consumers", key="submission_id", collection_name="general_store",
    )
else:
    raise RuntimeError("Must specify MongoDB URI containing inputs.")

# -- Tasks -- #

from emmet.api.routes.tasks.resources import (
    task_resource,
    trajectory_resource,
    entries_resource,
    task_deprecation_resource,
)

resources.update(
    {
        "tasks": [
            trajectory_resource(task_store),
            entries_resource(task_store),
            task_deprecation_resource(materials_store),
            task_resource(task_store),
        ]
    }
)

# -- Materials -- #

material_resources = []

from emmet.api.routes.materials.resources import (
    materials_resource,
    find_structure_resource,
    formula_autocomplete_resource,
)

material_resources.extend(
    [
        find_structure_resource(materials_store),
        formula_autocomplete_resource(formula_autocomplete_store),
        materials_resource(materials_store),
    ]
)


# Bonds
from emmet.api.routes.materials.bonds.resources import bonds_resource

material_resources.extend([bonds_resource(bonds_store)])


# Thermo
from emmet.api.routes.materials.thermo.resources import phase_diagram_resource, thermo_resource

material_resources.extend([phase_diagram_resource(phase_diagram_store), thermo_resource(thermo_store)])

# Dielectric
from emmet.api.routes.materials.dielectric.resources import dielectric_resource

material_resources.extend([dielectric_resource(dielectric_store)])

# Piezoelectric
from emmet.api.routes.materials.piezo.resources import piezo_resource

material_resources.extend([piezo_resource(piezoelectric_store)])

# Magnetism
from emmet.api.routes.materials.magnetism.resources import magnetism_resource

material_resources.extend([magnetism_resource(magnetism_store)])

# Phonon
from emmet.api.routes.materials.phonon.resources import phonon_bsdos_resource

material_resources.extend([phonon_bsdos_resource(phonon_bs_store)])

# EOS
from emmet.api.routes.materials.eos.resources import eos_resource

material_resources.extend([eos_resource(eos_store)])

# Similarity
from emmet.api.routes.materials.similarity.resources import similarity_resource

material_resources.extend([similarity_resource(similarity_store)])

# XAS
from emmet.api.routes.materials.xas.resources import xas_resource

material_resources.extend([xas_resource(xas_store)])

# Grain Boundaries
from emmet.api.routes.materials.grain_boundary.resources import gb_resource

material_resources.extend([gb_resource(gb_store)])

# Fermi Surface
from emmet.api.routes.materials.fermi.resources import fermi_resource

material_resources.extend([fermi_resource(fermi_store)])

# Elasticity
from emmet.api.routes.materials.elasticity.resources import elasticity_resource

material_resources.extend([elasticity_resource(elasticity_store)])

# DOIs
from emmet.api.routes.dois.resources import dois_resource

material_resources.extend([dois_resource(doi_store)])

# Substrates
from emmet.api.routes.materials.substrates.resources import substrates_resource

material_resources.extend([substrates_resource(substrates_store)])

# Surface Properties
from emmet.api.routes.materials.surface_properties.resources import surface_props_resource

material_resources.extend([surface_props_resource(surface_props_store)])

# Robocrystallographer
from emmet.api.routes.materials.robocrys.resources import robo_resource, robo_search_resource

material_resources.extend([robo_search_resource(robo_store), robo_resource(robo_store)])

# Synthesis
from emmet.api.routes.synthesis.resources import synth_resource

material_resources.extend([synth_resource(synth_store)])

# Electrodes
from emmet.api.routes.materials.electrodes.resources import insertion_electrodes_resource

material_resources.extend([insertion_electrodes_resource(insertion_electrodes_store)])

# Oxidation States
from emmet.api.routes.materials.oxidation_states.resources import oxi_states_resource

material_resources.extend([oxi_states_resource(oxi_states_store)])

# Alloys
from emmet.api.routes.materials.alloys.resources import alloy_pairs_resource

material_resources.extend([alloy_pairs_resource(alloy_pairs_store)])

# Provenance
from emmet.api.routes.materials.provenance.resources import provenance_resource

material_resources.extend([provenance_resource(provenance_store)])

# Charge Density
from emmet.api.routes.materials.charge_density.resources import (
    charge_density_resource,
    charge_density_url_resource,
)

material_resources.extend([charge_density_resource(s3_chgcar), charge_density_url_resource(chgcar_url)])

# Summary
from emmet.api.routes.materials.summary.resources import summary_resource, summary_stats_resource

material_resources.extend([summary_stats_resource(summary_store), summary_resource(summary_store)])

# Electronic Structure
from emmet.api.routes.materials.electronic_structure.resources import (
    es_resource,
    bs_resource,
    bs_obj_resource,
    dos_resource,
    dos_obj_resource,
)

material_resources.extend(
    [
        bs_resource(es_store),
        dos_resource(es_store),
        es_resource(es_store),
        bs_obj_resource(s3_bs),
        dos_obj_resource(s3_dos),
    ]
)

resources.update({"materials": material_resources})

# -- Molecules -- #
from emmet.api.routes.molecules.resources import molecules_resource

resources.update({"molecules": [molecules_resource(molecules_store)]})

# -- MPComplete -- #
from emmet.api.routes.mpcomplete.resources import mpcomplete_resource

resources.update({"mpcomplete": [mpcomplete_resource(mpcomplete_store)]})

# -- Consumers -- #
from emmet.api.routes._consumer.resources import settings_resource

resources.update({"_user_settings": [settings_resource(consumer_settings_store)]})

# -- General Store -- #
from emmet.api.routes._general_store.resources import general_store_resource

resources.update({"_general_store": [general_store_resource(general_store)]})

# === MAPI setup
from emmet.api.core.documentation import description, tags_meta

api = MAPI(resources=resources, debug=debug, description=description, tags_meta=tags_meta)
app = api.app
