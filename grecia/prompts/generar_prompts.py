"""Writes the 74 image prompts (imgN.txt) and the 18 Veo prompts (animN.txt) for the Greece long video (16:9)."""
import os

D = os.path.dirname(os.path.abspath(__file__))
N = ("IMPORTANT: Do not copy ANY element or character from the reference image. Use the uploaded image ONLY as an "
     "art style reference (round WHITE cartoon faces with simple expressive eyes, thick black outlines, flat colors). ")
S = (" Style: 2D cartoon like a history explainer animation, thick black outlines, flat colors with soft shading, "
     "highly detailed epic painted background with rich atmospheric lighting. All people have round white cartoon faces "
     "with simple eyes. No glow outline. No text, no letters, no numbers, no inscriptions, no signs, no watermark. "
     "Horizontal 16:9 widescreen.")

ALEX = "young ALEXANDER THE GREAT (clean shaven, wavy golden-blond hair, golden muscle cuirass, red cloak)"
LEON = "LEONIDAS (bronze Corinthian helmet with a tall red crest, short black beard, red cloak, big plain bronze round shield)"
PER = "PERICLES (short grey beard, bronze Corinthian helmet pushed up on his head, white and blue himation)"
SOC = "SOCRATES (bald head, big bushy grey beard, snub nose, simple worn grey robe, barefoot)"
DAR = "DARIUS (Persian king, tall golden crown, long curled black beard, purple and gold robes)"

SCENES = {
    1: "an epic rocky Greek coastline at golden sunset: steep mountains, turquoise sea, olive trees, a few cartoon goats standing on the rocks in the foreground, and far away on a hill the Acropolis of Athens with the Parthenon glowing.",
    2: "a grand modern parliament building with a classical Greek facade of white columns and a triangular pediment, and next to it an ancient-style open-air theater full of modern cartoon people, sunny day.",
    3: "an aerial view of the island of Crete in the shining blue Aegean Sea, mountains in the center, small ancient ships with sails around it, dawn light, clouds.",
    4: "an epic panoramic collage composed as one painting: on the left a red Minoan palace by the sea, in the middle a Spartan hoplite with a red cloak and a young golden-haired king on a black horse, on the right a line of Roman legionaries with red shields, under a dramatic sky.",
    5: "the huge Minoan palace of Knossos on a green hill on Crete, with red columns that are wider at the top, terraces, staircases and colorful walls, the blue sea behind, Minoan people in colorful clothes walking around.",
    6: "inside the palace of Knossos: a bright hall with red tapering columns, walls painted with colorful frescoes of blue dolphins and fish, a stone water channel with running water, Minoan women in colorful flounced dresses.",
    7: "a Minoan bull-leaping show in a palace courtyard: a young acrobat in a short loincloth flips through the air above the horns of a charging black bull, another acrobat waits behind, a cheering crowd on balconies.",
    8: "a dark stone labyrinth of endless corridors lit by a single torch, and at the end of a corridor the huge menacing shadow of the Minotaur, a man with a bull's head, on the wall. Mysterious, no gore.",
    9: "the gigantic volcanic eruption of the island of Thera seen from the sea: a huge column of ash and fire rising into the sky, lava, ash clouds, small ancient ships fleeing on rough waves.",
    10: "the Lion Gate of Mycenae: a massive gate made of gigantic stone blocks with two carved stone lions on top, cyclopean walls on a rocky hill, Mycenaean warriors with boar-tusk helmets and tall tower shields guarding it.",
    11: "a huge fleet of ancient Greek black ships with oars and square sails arriving at a beach, with the tall walls and towers of the city of Troy on a hill in the distance, warriors jumping onto the sand.",
    12: "night in front of the closed gates of Troy: a gigantic wooden horse on wheels stands on the plain, torches on the city walls, Trojan guards on the walls looking down at it curiously, moonlight.",
    13: "a great Mycenaean palace burning at dusk, flames and black smoke rising from the roofs and columns, people running away in the distance, red sky. No gore.",
    14: "a poor little village of simple mud huts next to the abandoned ruins of a great stone palace overgrown with weeds, a shepherd with goats, grey cloudy sky, melancholic.",
    15: "night in a village: an old bard with a lyre sings by a big campfire, villagers of all ages sit around listening with wide eyes, sparks flying up into the starry sky.",
    16: "a busy ancient port: a Phoenician merchant with a purple robe and a pointed cap shows a clay tablet to a curious Greek scribe, ships with eye-painted bows in the harbor, amphorae and crates.",
    17: "the blind poet HOMER (old man, long white beard, closed eyes, white robe, laurel wreath) sitting under an olive tree playing a lyre, behind him the ghostly images of warriors and ships in the clouds, golden light.",
    18: "an epic wide landscape of ancient Greece: mountains and bays, and many separate small walled cities with temples on hilltops, each with its own colored banner, ships sailing between them.",
    19: "two ancient Greek hoplite phalanxes facing each other on a plain, bronze helmets, big round shields with different colors (blue against red), long spears lowered, dust in the air.",
    20: "ancient Greek ships arriving at a new Mediterranean coast, colonists unloading amphorae, building the first walls and a small temple on a hill above a bay, green hills, sunny.",
    21: "the valley of ancient Sparta under the towering mountains of Taygetus, simple villages without walls, fields, and a group of Spartan warriors in red cloaks marching on a road.",
    22: "young Spartan men (teenagers) training hard in a dusty field: wrestling, running with heavy shields, a stern Spartan instructor with a red cloak and a stick watching, mountains behind.",
    23: "the busy agora of Athens: market stalls with pottery, olives and fish, merchants, sailors, artists and philosophers arguing with big gestures, temples and the Acropolis above, sunny.",
    24: "the Greek gods on top of Mount Olympus above the clouds: ZEUS (big white beard, thunderbolt), Hera, Athena with a helmet, Poseidon with a trident, Apollo with a lyre, on golden thrones, epic heavenly light.",
    25: "a foot race in the ancient stadium of Olympia: naked-looking athletes shown in short white loincloths running fast on the sand track, a huge crowd cheering on the grassy slopes, the temple of Zeus behind.",
    26: "a contrast scene in ancient Athens: rich aristocrats in fine purple robes feasting on a hill under a temple, and below, poor farmers with rags working dry fields, looking tired.",
    27: "SOLON (wise man, grey beard, white robe) standing on steps reading new laws from big wooden tablets to a large crowd of Athenian citizens who cheer, in front of a temple.",
    28: "CLEISTHENES (dark curly beard, white and green robe) speaking from a stone speaker's platform on the Pnyx hill to the assembly of Athenian citizens, the Acropolis in the background, sunny.",
    29: "Athenian citizens in a line dropping broken pieces of pottery (ostraka, blank, no writing visible) into a large clay urn, an official watching, the agora behind.",
    30: "the Athenian assembly of men voting with raised hands, while at the edge, women, foreign merchants and servants watch from outside a low wall with unhappy faces.",
    31: f"the grand palace of Persepolis with tall stone columns topped by bull capitals, King {DAR} sitting on a golden throne, guards with tall spears, and a huge crowd of subjects bringing gifts.",
    32: "a huge Persian fleet landing on the beach of Marathon: hundreds of ships, Persian soldiers in colorful tunics and soft caps with wicker shields coming ashore, mountains around the plain.",
    33: "the Athenian hoplites charging at a run across the plain of Marathon, bronze helmets and round shields, spears forward, dust behind them, the Persian army ahead, dramatic sky.",
    34: "a lone exhausted Greek runner in a short tunic running along a dusty mountain road toward the distant city of Athens and the Acropolis, sunset, olive trees.",
    35: "the gigantic army of the Persian king XERXES (tall golden crown, long curled black beard) crossing a long bridge of boats over the Hellespont strait, endless lines of soldiers, horses and banners to the horizon.",
    36: f"the narrow pass of Thermopylae between steep cliffs and the sea: {LEON} stands in front of his Spartans in red cloaks with locked shields, calm and ready, morning light.",
    37: "Persian soldiers in colorful tunics sneaking at night along a narrow mountain path behind the Greek lines, guided by a Greek traitor in a brown cloak with a torch, moonlight, dark forest.",
    38: "the city of Athens burning on the horizon at night, seen from the sea, while in the foreground Athenian families stand on the decks of their trireme ships, watching sadly.",
    39: "the naval battle of Salamis in a narrow strait: Greek triremes with bronze rams crash into big Persian ships, oars breaking, splashes, smoke, islands on both sides. No blood.",
    40: "victorious Greek warriors and sailors cheering on a beach at sunset, raising their spears and shields, the remains of the Persian fleet sinking far away on the sea.",
    41: f"{PER} standing on a terrace looking proudly over the city of Athens at sunrise, the Acropolis hill in front of him, architects showing him plans.",
    42: "the construction of the Parthenon on the Acropolis: wooden scaffolding, cranes with ropes, workers lifting white marble column drums, sculptors carving, the city below.",
    43: "inside the newly built Parthenon: the gigantic 12-meter statue of the goddess Athena covered in gold and ivory, holding a small winged Nike in her hand and a big shield, the temple walls painted in bright colors, tiny visitors in awe.",
    44: "a huge ancient Greek open-air theater full of spectators on stone steps, on stage actors wearing big tragedy and comedy masks, some spectators crying and others laughing.",
    45: "HIPPOCRATES (bald, white beard, white robe) calmly examining a patient lying on a bed, scrolls and herbs on a table, a student taking notes, a temple courtyard outside.",
    46: f"{SOC} in the agora of Athens asking questions to a confused young aristocrat, a small crowd of students and curious people around them, columns and market stalls behind.",
    47: f"{SOC} in a stone prison cell holding a cup, calm and serene, surrounded by his sad students and friends, light coming from a small window.",
    48: "PLATO (white beard, pink robe) and his student ARISTOTLE (short brown beard, blue robe) walking and discussing in a grand hall with arches, Plato pointing up and Aristotle pointing down, students around.",
    49: "a tense confrontation: on the left the great Athenian fleet of triremes in a harbor, on the right the Spartan army in red cloaks on a hill, both sides glaring at each other, stormy sky.",
    50: "two Greek hoplite armies clashing shield against shield in a big dusty battle, Athenians with blue shields against Spartans with red cloaks. No blood.",
    51: "the crowded city of Athens inside its walls under a dark gloomy sky, tents and refugees everywhere, sad and sick people resting, smoke, a feeling of plague. No gore, no bodies.",
    52: "a disaster at sea near the coast of Sicily: Athenian triremes broken and sinking, sailors swimming, a Syracusan fleet closing in, Mount Etna smoking in the background. No blood.",
    53: "Spartan soldiers in red cloaks pulling down the Long Walls of Athens with ropes while flute players play, Athenians watching sadly, the Acropolis behind.",
    54: "a sad landscape of ancient Greece after the war: burned fields, a ruined small town, a lonely broken column, crows, grey sky.",
    55: "the king of Macedonia PHILIP II (black beard, eye patch over one eye, purple cloak, golden helmet) on a horse on a mountain top, looking down at the Greek cities in the distance, his soldiers behind him.",
    56: "the Macedonian phalanx advancing: rows of soldiers holding extremely long spears (sarissas) pointing forward like a wall of spikes, small round shields, marching across a plain, dust.",
    57: f"the philosopher ARISTOTLE (short brown beard, blue robe) teaching a teenage {ALEX} under a tree in a garden, scrolls on a stone bench, other students listening.",
    58: f"a teenage {ALEX} holding the reins of a huge wild black horse (Bucephalus) with a white star on its forehead, turning its head toward the sun, the horse rearing up, King Philip and the court watching amazed.",
    59: f"{ALEX} standing at the bow of a ship crossing the Hellespont, throwing a spear onto the shore of Asia, behind him a large fleet full of Macedonian soldiers, sunrise.",
    60: f"the battle of Gaugamela on a vast dusty plain: {ALEX} on his black horse charges with his cavalry, while the Persian king {DAR} flees in a golden chariot, huge Persian army. No blood.",
    61: f"{ALEX} in Egypt standing near the pyramids and the Nile, Egyptian priests bowing to him, while architects mark the plan of a new city by the sea with a line of flour on the ground.",
    62: "the battle against King Porus in India: huge armored war elephants with towers on their backs charge against the Macedonian phalanx with long spears, monsoon clouds, a river. No blood.",
    63: f"{ALEX} standing on a high mountain at sunset, his red cloak flying in the wind, looking over an endless landscape of deserts, rivers and mountains stretching to the horizon.",
    64: "exhausted Macedonian soldiers sitting in the mud under heavy monsoon rain, refusing to march, their shields lowered, while their general looks at them from his horse.",
    65: f"{ALEX}, pale and weak, lying on a bed in a Babylonian palace, surrounded by his worried generals who lean in to hear him, oil lamps, a sad mood.",
    66: "the Macedonian generals arguing and shouting around a big table with a painted map of the empire, one pulling the map, another pointing a dagger at it, comedic tension.",
    67: "a Hellenistic city in Central Asia: a Greek temple with columns next to oriental domed buildings, Greek and Asian people mixing in the market, camels, snowy mountains behind.",
    68: "the gigantic Lighthouse of Alexandria at night, a tall stone tower with a huge fire on top shining over the sea, ships entering the harbor, and on the shore the great library with columns.",
    69: "ARCHIMEDES (wild grey hair and beard) jumping out of a bathtub full of water with a happy shocked face, water splashing everywhere, a servant dropping a towel in surprise. Comedic, wearing a towel, no nudity.",
    70: "Roman legionaries with red rectangular shields and crested helmets marching into the burning Greek city of Corinth, temples and columns, smoke in the sky. No blood.",
    71: "rich Roman nobles in white togas admiring and buying beautiful Greek marble statues and painted vases in a villa garden, a Greek teacher reading to Roman children.",
    72: "a modern Olympic stadium at night full of fans, the Olympic flame burning in a big cauldron, fireworks, an athlete running with the torch.",
    73: "the rocky Greek hills at golden sunset, a few cartoon goats on the rocks in the foreground, and in the distance the Parthenon on the Acropolis glowing, the sea shining.",
    74: "the Parthenon on the Acropolis at night under a sky full of stars and the Milky Way, softly lit, the lights of the city below, calm and majestic.",
}

B = ("This image is the exact first frame. Keep everything identical to it: same composition, same 2D hand-drawn cartoon "
     "art style with thick black outlines and flat colors, same characters with round white cartoon faces. Do NOT make "
     "anything realistic, do NOT redesign or change any character, do NOT add any new object, do NOT cut to another shot. "
     "Smooth, fluid 2D cartoon animation with small, natural movements and lively visual effects. No text on screen. "
     "Audio: sound effects and ambience only, absolutely NO voices, NO dialogue, NO narration, NO singing, NO music. "
     "STRICT RULES: no fire unless already in the image. ")
ANIM = {
    1: "Action: the goats move their heads and chew, the olive trees sway, waves break on the rocks. Camera: slow push-in toward the Acropolis. Audio: sea waves, wind, a goat bell.",
    7: "Action: the acrobat completes the flip over the bull's horns and lands, the bull keeps running, the crowd raises its arms. Camera: slight follow pan. Audio: bull hooves, crowd cheering without words.",
    9: "Action: the volcano erupts, the ash column grows and rolls, lava glows, the ships row away on the waves. Camera: slight shake and slow pull back. Audio: deep rumble, explosions, waves.",
    12: "Action: the torches flicker, the guards on the wall point at the horse and look at each other, the moon moves behind clouds. Camera: slow push-in toward the horse. Audio: night wind, crackling torches, crickets.",
    24: "Action: Zeus raises his thunderbolt that crackles with light, the gods turn their heads, the clouds roll. Camera: slow push-in toward Zeus. Audio: thunder rumble, wind.",
    25: "Action: the runners race along the track, the crowd jumps and cheers. Camera: tracking pan following the runners. Audio: running feet on sand, crowd cheering without words.",
    33: "Action: the hoplites charge forward at a run, shields and spears bouncing, dust rising. Camera: slight shake following the charge. Audio: running footsteps, clanking armor, war horns.",
    35: "Action: the endless army marches across the bridge of boats, the boats rock on the water, banners wave. Camera: slow pan along the bridge. Audio: marching feet, waves, horses.",
    37: "Action: the soldiers walk carefully in a line along the path, the traitor's torch flickers, owls watch. Camera: slow pan following them. Audio: soft footsteps, night insects, wind.",
    39: "Action: the Greek triremes ram the Persian ships, oars splinter, water splashes, ships tilt. Camera: slight shake and slow push-in. Audio: wood cracking, splashes, horns.",
    43: "Action: light rays move across the golden statue, it sparkles, the tiny visitors look up and point. Camera: slow tilt up the statue. Audio: echo of a temple, soft wind.",
    56: "Action: the phalanx marches forward in step, the long spears sway together, dust rises. Camera: low slow push-in toward the spears. Audio: marching feet, clanking, drums.",
    58: "Action: the horse calms down, lowers its front legs, Alexander strokes its neck and smiles, the court cheers. Camera: slow push-in. Audio: horse neighing and snorting, hooves.",
    60: "Action: Alexander's cavalry charges, the Persian king's chariot speeds away, dust clouds billow. Camera: slight shake and pan. Audio: galloping, battle horns, wheels.",
    62: "Action: the elephants charge and raise their trunks, the phalanx braces with spears, rain falls. Camera: slight shake. Audio: elephants trumpeting, rain, clashing.",
    68: "Action: the fire on top of the lighthouse flickers and its light sweeps over the sea, ships sail into the harbor, waves move. Camera: slow push-in. Audio: waves, wind, ship creaking.",
    70: "Action: the legionaries march forward in step, smoke rises, banners wave. Camera: slow pan. Audio: marching, distant crackling, horns.",
    73: "Action: the goats move and chew, the sun sets slowly, the sea sparkles, birds fly. Camera: slow pull back. Audio: wind, goat bell, distant waves.",
}

for n, s in SCENES.items():
    open(f"{D}/img{n}.txt", "w").write(N + "Scene: " + s + S)
for n, a in ANIM.items():
    open(f"{D}/anim{n}.txt", "w").write(B + a)
print(len(SCENES), "imágenes,", len(ANIM), "animaciones")
