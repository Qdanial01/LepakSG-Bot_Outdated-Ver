from random import choice


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'ang mo kio' in lowered:
        return choice(['Brew & Co.', 'Ang Mo Kio Park', 'AMK Hub'])
    elif 'bedok' in lowered:
        return choice(['Bedok Mall', 'Bedok Jetty', 'Bedok Maze'])
    elif 'bishan' in lowered:
        return choice(['Windsor Nature Park', 'Thomson Plaza', 'Kings Cart Coffee'])
    elif 'bugis' in lowered:
        return choice(['Kampong Glam Cafe', 'Rumi', 'Chix Hot Chicken'])
    elif 'bukit batok' in lowered:
        return choice(['Bukit Batok Nature Park', 'Coexist Coffee Co', 'West Mall'])
    elif 'bukit merah' in lowered:
        return choice(['Vivo City', 'Henderson Wave', 'Labrador Nature Reserve'])
    elif 'bukit panjang' in lowered:
        return choice(['Junction 10', 'Bukit Timah Nature Reserve', 'Hillion Mall'])
    elif 'chao chu kang' in lowered:
        return choice(['Lot One', 'SAFRA Bowling', 'Teck Whye Garden'])
    elif 'clementi' in lowered or 'west coast' in lowered:
        return choice(['Clementi Mall', 'West Coast Park', 'Burnt Cones'])
    elif 'geylang' in lowered:
        return choice(['Geylang Serai', 'Joo Chiat Complex', 'Paya Lebar Square', '89.7 Supper Club'])
    elif 'hougang' in lowered:
        return choice(['Hougang Mall', 'Maplewood Park', 'Lola\'s Cafe'])
    elif 'jurong east' in lowered:
        return choice(['Jem/Westgate', 'Padi Emas', 'Imm'])
    elif 'jurong west' in lowered:
        return choice(['Jurong Point', 'Lakeside', 'Al-Ayza'])
    elif 'kallang' in lowered or 'whampoa' in lowered:
        return choice(['Stadium', 'Decathlon', 'City Square Mall'])
    elif 'pasir ris' in lowered:
        return choice(['Pasir Ris Park', 'White Sands Mall, Downtown East', '89.7 Supper Club'])
    elif 'punggol' in lowered:
        return choice(['Punggol Beach', 'Tebing Lane', 'Hai Bin'])
    elif 'queenstown' in lowered:
        return choice(['Queensway', 'ABC', 'Star Vista'])
    elif 'sembawang' in lowered:
        return choice(['Sun Plaza', 'Sembawang Park', 'Canberra Plaza'])
    elif 'sengkang' in lowered:
        return choice(['Seletar Mall', 'Compass One', 'Rivervale Mall'])
    elif 'serangoon' in lowered:
        return choice(['Nex', 'Coney Island Park', 'Nim Meadow Park'])
    elif 'tampines' in lowered:
        return choice(['Tampiness', 'Changi City Point', 'Tampiness Hub'])
    elif 'tengah' in lowered:
        return choice(['Plantation Plaza', 'Garden Vines', 'Le Quest Shopping Mall'])
    elif 'toa payoh' in lowered:
        return choice(['Toa Payoh Town Park', 'Creamier', 'Woodleigh Mall'])
    elif 'woodlands' in lowered:
        return choice(['Causewaypoint', 'Woodlands Waterfront Park', 'Al-Ameen', 'Citrus By the Pool'])
    elif 'yishun' in lowered:
        return choice(['Northpoint City', 'Junction Nine', 'Wisteria Mall'])
    elif 'bukit timah' in lowered:
        return choice(['Al-Azhar Restaurant', 'Bukit Timah Plaza', 'Atlas Coffeehouse'])
    elif 'marine parade' in lowered:
        return choice(['Parkway Parade', 'East Coast Park', 'Cafe Melba'])
    elif 'Central Area' in lowered:
        return choice(['Somerset', 'MBS', 'Funan'])
    else:
        return choice(['bye', 'see ya!'])