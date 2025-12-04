from database.repository import add_interaction, get_all_interactions
from database.models import Interaction

inter = Interaction(id=None, medication1="Paracetamol", medication2="Ibuprofen",
                    interaction_level="Moderate", description="May increase liver risk")
add_interaction(inter)

print(get_all_interactions())

