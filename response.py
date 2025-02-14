from random import choice

# Pre-generated message list
Reply_List = [
    "{} seems like a great option for today!",
    "How about checking out {}? It's a great place to chill!",
    "{} could be fun spot to rest and relax!",
    "I heard {} is a great place to go!",
    "Maybe try {}? It's a popular choice for some people!",
    "If you're looking for something to just lepak, {} is one of recommended picks!",
    "{} sounds like a cozy place to just chill!",
    "I would suggest going to {}!",
    "{} is a good spot!",
    "{} is a great place to relax!"
]


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return 'Well, you\'re awfully quiet....'
    elif lowered == 'lepaksg':
        return 'Hi there! Which town are you planning to lepak at?'

    # Dictionary for recommended spots
    Recommended_Spots = {
    'ang mo kio': ['Brew & Co.', 'Ang Mo Kio Park', 'AMK Hub'],
    'bedok': ['Bedok Mall', 'Bedok Jetty', 'Bedok Maze'],
    'bishan': ['Windsor Nature Park', 'Thomson Plaza', 'Kings Cart Coffee'],
    'bugis': ['Kampong Glam Cafe', 'Rumi', 'Chix Hot Chicken'],
    'bukit batok': ['Bukit Batok Nature Park', 'Coexist Coffee Co', 'West Mall'],
    'bukit merah': ['Vivo City', 'Henderson Wave', 'Labrador Nature Reserve'],
    'bukit panjang':['Junction 10', 'Bukit Timah Nature Reserve', 'Hillion Mall'],
    'chao chu kang': ['Lot One', 'SAFRA Bowling', 'Teck Whye Garden'],
    'clementi': ['Clementi Mall', 'West Coast Park', 'Burnt Cones'],
    'west coast':['Clementi Mall', 'West Coast Park', 'Burnt Cones'],
    'geylang': ['Geylang Serai', 'Joo Chiat Complex', 'Paya Lebar Square', '89.7 Supper Club'],
    'hougang': ['Hougang Mall', 'Maplewood Park', 'Lola\'s Cafe'],
    'jurong east': ['Jem/Westgate', 'Padi Emas', 'Imm'],
    'jurong west': ['Jurong Point', 'Lakeside', 'Al-Ayza'],
    'kallang': ['Stadium', 'Decathlon', 'City Square Mall'],
    'whampoa': ['Stadium', 'Decathlon', 'City Square Mall'],
    'pasir ris': ['Pasir Ris Park', 'White Sands Mall, Downtown East', '89.7 Supper Club'],
    'punggol': ['Punggol Beach', 'Tebing Lane', 'Hai Bin'],
    'queenstown': ['Queensway', 'ABC', 'Star Vista'],
    'sembawang': ['Sun Plaza', 'Sembawang Park', 'Canberra Plaza'],
    'sengkang': ['Seletar Mall', 'Compass One', 'Rivervale Mall'],
    'serangoon': ['Nex', 'Coney Island Park', 'Nim Meadow Park'],
    'tampines': ['Tampines Mall', 'Changi City Point', 'Tampines Hub'],
    'tengah': ['Plantation Plaza', 'Garden Vines', 'Le Quest Shopping Mall'],
    'toa payoh': ['Toa Payoh Town Park', 'Creamier', 'Woodleigh Mall'],
    'woodlands': ['Causewaypoint', 'Woodlands Waterfront Park', 'Al-Ameen', 'Citrus By the Pool'],
    'yishun': ['Northpoint City', 'Junction Nine', 'Wisteria Mall'],
    'bukit timah': ['Al-Azhar Restaurant', 'Bukit Timah Plaza', 'Atlas Coffeehouse'],
    'marine parade': ['Parkway Parade', 'East Coast Park', 'Cafe Melba'],
    'Central Area': ['Somerset', 'MBS', 'Funan']
    } 

    # Check if user input contains any known towns
    for location, places in Recommended_Spots.items():
        if location in lowered:
            place = choice(places) # A spot is chosen at random depending on the selected town
            message = choice(Reply_List).format(place) # Format with a pre-written reply
            return message
    
    return choice(["Im not sure where that is, my developer half fuck my code so my process is a bit limited.",
                   "Hmm, I don't have info on that, but let me know if I should add it!"])