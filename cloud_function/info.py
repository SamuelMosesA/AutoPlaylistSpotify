class Genre:
    def __init__(self, genlist):
        self.genres = genlist

    def __eq__(self, value):
        for ele in self.genres:
            if ele in value.genres:
                return True
        return False


# genres
c_rap_genres = Genre(['christian hip hop', 'rap rock', 'christian trap',
                      'rap metal', 'alternative hip hop',
                      'hip hop', 'pop rap'])

ambient_study_genres = Genre(['chillhop', 'instrumental rock', 'lo-fi beats', 'chillstep', 'new age',
                              'electronica', 'ambient', 'downtempo',
                              'indie electropop', 'vapour soul', 'deep house',
                              'catstep', 'livetronica', 'chillwave', 'bass music',
                              'beach house', 'focus', 'atmospheric post-rock',
                              'background music', 'compositional ambient', 'electro swing',
                              'calming instrumental', 'indie soul', 'indie jazz', 'melodic dubstep',
                              'jazztronica', 'japanese chillhop', 'american post-rock', 'british post-rock',
                              'progressive house', 'flamenco', 'chill guitar', 'bristol electronic',
                              'japanese instrumental', 'folkmusik', 'new french touch'])

c_rock_genres = Genre(['christian rock', 'post-grunge',
                       'rap rock', 'pop rock', 'modern alternative rock', 'modern rock', 'alternative metal'])

scottish_folk_genres = Genre(
    ['scottish folk', 'jig and reel', 'celtic', 'irish folk', 'irish neo-traditional', 'concertina',
     'uilleann pipes'])

carnatic_fusion_genres = Genre(['indian classical', 'neo-classical', 'indian folk', 'world folk', 'world fusion',
                                'hindustani classical', 'indian jazz', 'indian rock', 'sitar', 'sufi', 'indian indie',
                                'bansuri', 'afropop', 'arab folk'])

ccm_genres = Genre(
    ['ccm', 'christian pop', 'anthem worship', 'world worship', 'acoustic pop',
     'christian relaxative', 'cedm', 'baptist gospel', 'ambient worship', 'christian alternative rock'])

# playlist ids

rap_playlist_id = '0OcZwoiZ2LMKWpYFuP5QaA'
ambient_playlist_id = '3rmNGYBHSiqMu5sZOCzQyc'
scottish_playlist_id = '7z282Qn6tSJqEbeGdZCnXE'
rock_playlist_id = '19LEEBmbpLm34fEg9AhlBJ'
carnatic_playlist_id = '6fS9KlKycuyyPBEZIpyyL0'
ccm_playlist_id = '1e3wh8d2IgwLAVTVQfWfzz'
