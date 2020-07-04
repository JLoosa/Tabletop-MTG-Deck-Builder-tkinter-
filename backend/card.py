

# The Scryfall website API page states that results are REST-ful, and itemizes the fields that can be expected.
# The following class is a wrapper around the json data that comes from the Scryfall site
class Card:

    # TODO: Privatize the fields and implement accessors and mutators
    def __init__(self, json_object: dict):
        # Core Card Fields (Non-Nullable)
        self.id = json_object["id"]
        self.lang = json_object["lang"]
        self.oracle_id = json_object["oracle_id"]
        self.prints_search_uri = json_object["prints_search_uri"]
        self.rulings_uri = json_object["rulings_uri"]
        self.scryfall_uri = json_object["scryfall_uri"]
        self.uri = json_object["uri"]
        # Core Card Fields (Nullable)
        self.arena_id = json_object["arena_id"]
        self.mtgo_id = json_object["mtgo_id"]
        self.mtgo_foil_id = json_object["mtgo_foil_id"]
        self.multiverse_ids = json_object["multiverse_ids"]
        self.tcgplayer_id = json_object["tcgplayer_id"]
        # Gameplay Fields (Non-Nullable)
        self.cmc = json_object["cmc"]
        self.color_identity = json_object["color_identity"]
        self.foil = json_object["foil"]
        self.keywords = json_object["keywords"]
        self.layout = ["layout"]
        self.legalities = json_object["legalities"]
        self.name = json_object["name"]
        self.nonfoil = json_object["nonfoil"]
        self.type_line = json_object["type_line"]
        self.oversized = json_object["oversized"]
        self.reserved = json_object["reserved"]
        # Gameplay Fields (Nullable)
        self.all_parts = json_object["all_parts"]
        self.card_faces = json_object["card_faces"]
        self.color_indicator = json_object["color_indicator"]
        self.colors = json_object["colors"]
        self.edhrec_rank = json_object["edhrec_rank"]
        self.hand_modifier = json_object["hand_modifier"]
        self.life_modifier = json_object["life_modifier"]
        self.loyalty = json_object["loyalty"]
        self.mana_cost = json_object["mana_cost"]
        self.oracle_text = json_object["oracle_text"]
        self.power = json_object["power"]
        self.produced_mana = json_object["produced_mana"]
        self.toughness = json_object["toughness"]
        # Print Fields (Non-Nullable)
        self.booster = json_object["booster"]
        self.border_color = json_object["border_color"]
        self.card_back_id = json_object["card_back_id"]
        self.collector_number = json_object["collector_number"]
        self.digital = json_object["digital"]
        self.frame = json_object["frame"]
        self.full_art = json_object["full_art"]
        self.games = json_object["games"]
        self.highres_image = json_object["highres_image"]
        self.prices = json_object["prices"]
        self.promo = json_object["promo"]
        self.purchase_uris = json_object["purchase_uris"]
        self.rarity = json_object["rarity"]
        self.related_uris = json_object["related_uris"]
        self.released_at = json_object["released_at"]
        self.reprint = json_object["reprint"]
        self.scryfall_set_uri = json_object["scryfall_set_uri"]
        self.set_name = json_object["set_name"]
        self.set_search_uri = json_object["set_search_uri"]
        self.set_type = json_object["set_type"]
        self.set_uri = json_object["set_uri"]
        self.set = json_object["set"]
        self.story_spotlight = json_object["story_spotlight"]
        self.textless = json_object["textless"]
        self.variation = json_object["variation"]
        # Print Fields (Nullable)
        self.artist = json_object["artist"]
        self.content_warning = json_object["content_warning"]
        self.flavor_name = json_object["flavor_name"]
        self.flavor_text = json_object["flavor_text"]
        self.frame_effects = json_object["frame_effects"]
        self.illustration_id = json_object["illustration_id"]
        self.image_uris = json_object["image_uris"]
        self.printed_name = json_object["printed_name"]
        self.printed_text = json_object["printed_text"]
        self.printed_type_line = json_object["printed_type_line"]
        self.promo_types = json_object["promo_types"]
        self.variation_of = json_object["variation_of"]
        self.watermark = json_object["watermark"]
        self.preview_previewed_at = json_object["preview.previewed_at"]
        self.preview_source_uri = json_object["preview.source_uri"]
        self.preview_source = json_object["preview.source"]


# Cards may have multiple card faces. The following class describes them following the same format that the Scryfall site uses
class CardFace:

    def __init__(self, json_object: dict):
        # Non-Nullable Fields
        self.mana_cost = json_object["mana_cost"]
        self.name = json_object["name"]
        self.object = json_object["object"]
        self.type_line = json_object["type_line"]
        # Nullable Fields
        self.artist = json_object["artist"]
        self.color_indicator = json_object["color_indicator"]
        self.colors = json_object["colors"]
        self.flavor_text = json_object["flavor_text"]
        self.illustration_id = json_object["illustration_id"]
        self.image_uris = json_object["image_uris"]
        self.loyalty = json_object["loyalty"]
        self.oracle_text = json_object["oracle_text"]
        self.power = json_object["power"]
        self.printed_name = json_object["printed_name"]
        self.printed_name = json_object["printed_text"]
        self.printed_name = json_object["printed_type_line"]
        self.toughness = json_object["toughness"]
        self.watermark = json_object["watermark"]


# Similar to the CardFaces section, this class decribes a single RelatedCard object
class RelatedCard:

    def __init__(self, json_object: dict):
        # All fields will be non-nullable for this class
        self.id = json_object["id"]
        self.object = json_object["object"]
        self.component = json_object["component"]
        self.name = json_object["name"]
        self.type_line = json_object["type_line"]
        self.uri = json_object["uri"]


# After we know what a card is, we can consider an object that would be responsible to storing them
# TODO: Consider using a singleton for the CardCollection, as having multiple seems like nonsense
class CardCollection:

    def __init__(self, card_list_json: list):
        self.cards = None
        self.load_cards(card_list_json)

    def load_cards(self, card_list_json: list):
        # We can do this with list comprehension pretty easily.
        # TODO: Consider a try/except here in the event one or more bad entries
        card_generator = (Card(json_object=json) for json in card_list_json)
        # I used a generator function because I want to form them into a dict, and I only need to iterate through sequentially
        self.cards = {card.name: card for card in card_generator}
        print("Loaded card count:", len(self.cards))


# Now that we have a data structure to hold the cards, we can play with the idea of having a "Lookup" for them
class CardLookup:

    def __init__(self, collection: CardCollection):
        self.collection = collection

    def search_for_name(self, search_name: str):
        return (card for card_name, card in self.collection.cards.items() if search_name in card_name)

    def search_for_id(self, search_id: str):
        return (card for card in self.collection.cards.values() if search_id in card.id)

    # TODO: Implement other search functions as needed

# This is a variation of the normal CardLookup that will allow for "filters" to be placed on the underlying data set
# These filters will help reduce the number of results from that data set, and make deck building easier for the end-user
# An example filter would be something like "Set", and would allow the user to choose options such as "Throne of Eldraine / ELD"
# TODO: Implementation
class FilteredCardLookup(CardLookup):

    def __init__(self, collection: CardCollection):
        super(FilteredCardLookup, self).__init__(collection)
