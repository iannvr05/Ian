"""Genera img1.txt…img57.txt para 'Tu vida en el Cártel de Medellín' (16:9, imágenes estáticas)."""
import os
PRE = ("IMPORTANT: Do not copy ANY element or character from the reference image. Use the uploaded image ONLY as an "
       "art style reference (round white cartoon faces with simple expressive eyes, thick black outlines, flat colors). ")
POST = (" Setting: Medellin, Colombia, in the 1980s (modern era): people wear modern clothes like t-shirts, jeans, polo shirts and sneakers. Only include cars or city elements if the scene is in the city. Nothing medieval or colonial, no donkeys, no old-fashioned costumes, no aprons or headscarves. Style: 2D cartoon like a history explainer animation, thick black outlines, "
        "flat colors with soft shading, highly detailed painted background with rich atmospheric lighting. All people have "
        "round white cartoon faces with simple eyes. No glow outline. ABSOLUTELY NO TEXT anywhere: no words, no letters, "
        "no numbers, no logos, no brand names on vehicles or products, no labels on packages, all signs, posters, magazines, maps and screens blank. No blood, no gore, "
        "no guns pointed at anyone, no drugs or powder visible. No watermark. Horizontal 16:9 widescreen.")
BOY = "a skinny 12-year-old boy with short black hair, round white cartoon face, faded yellow t-shirt and blue shorts"
TEEN = "the same young man now 16, taller and thin, short black hair, round white cartoon face, yellow t-shirt and jeans"
PAB = "Pablo Escobar as a cartoon: a chubby man with curly black hair, thick black mustache, light blue polo shirt and jeans"
S = {
1: f"Scene: a poor hillside neighborhood (comuna) of unfinished red-brick houses stacked up a steep mountain at sunset; {BOY} leans out of a small window looking down at the huge city of Medellin glowing with lights in the valley far below. Epic orange sky and green Andes mountains.",
2: f"Scene: a narrow street of the hillside comuna; a man in sunglasses and a flowered shirt sits on a motorcycle in front of a humble brick house and, smiling, holds out a thick bundle of green banknotes toward {BOY} standing in the doorway.",
3: f"Scene: inside a humble brick house, {BOY} stares in amazement at a thick bundle of green banknotes in his hands in the foreground; in the background his exhausted father in dirty work clothes sits slumped on a plastic chair.",
4: "Scene: the city of Medellin at night seen from the mountains, thousands of lights in the valley, and a gigantic dark ominous shadow of a man's silhouette looming over the whole city like a giant in the sky. Dramatic, mysterious mood.",
5: "Scene: wide view of 1980s Medellin divided in two: on the steep mountainsides above, endless poor red-brick houses with tin roofs; down in the green valley, modern white high-rise buildings, wide avenues and swimming pools. Bright daylight, strong contrast.",
6: "Scene: a steep dirt street in the poor comuna; a dry public water tap with a line of people holding empty buckets; several barefoot kids sit idle on the curb with nothing to do; laundry hanging between brick houses.",
7: f"Scene: a small patio of a brick house; a tired mother scrubs clothes by hand in a concrete washing basin with piles of other people's laundry; the exhausted father arrives home at dusk with dusty work clothes; {BOY} watches them.",
8: f"Scene: a comuna street; two teenagers with new shiny sneakers and gold chains lean proudly on a new red motorcycle; a group of poor younger kids including {BOY} look at them with envy and admiration.",
9: "Scene: a narrow hillside street; neighbors peek silently from windows and half-open doors, some looking away, an old woman closing her shutters, a mysterious motorcycle parked in the street. Tense, silent mood.",
10: f"Scene: {BOY} sits on a low brick wall at a corner at the top of a very steep street, carefully watching who comes up the hill; the comuna and the city spread behind him.",
11: f"Scene: {BOY} on a street corner whistling loudly with two fingers in his mouth; far down the steep street a white and green police patrol car of the 1980s is coming up the hill.",
12: "Scene: a humble kitchen; a mother (woman with black hair in a ponytail) opens an old refrigerator that is completely full of unlabeled food (meat, fruit, eggs, vegetables) and looks sideways with a suspicious, worried expression.",
13: f"Scene: {BOY} walks confidently up a comuna street; other kids and young men greet him with respect, raising hands and nodding; a shopkeeper waves at him.",
14: "Scene: a large colorful painted mural on a brick wall of the comuna showing the face of a man with curly black hair and a thick mustache; people stand in front of it looking up with a mix of respect and fear.",
15: f"Scene: {PAB}, standing calm with hands in pockets in front of gigantic mountains of stacked green banknote bundles reaching the ceiling of a huge warehouse.",
16: f"Scene: {PAB}, sitting in a luxurious leather armchair, smiling proudly while holding up a business magazine with a blank cover; luxurious office.",
17: f"Scene: {PAB}, cutting a ribbon at the inauguration of a brand-new neighborhood football field with tall floodlights at night, happy poor kids playing football and crowds cheering on the hillside.",
18: "Scene: a city street wall covered with many identical wanted posters showing the face of a cartoon man with curly black hair and mustache (posters with no writing at all); a police car and policemen in the street; also an old 1980s TV in a shop window showing the same face.",
19: "Scene: an enormous tropical ranch (hacienda): a white entrance gate with a small vintage airplane mounted on top of it, green hills, a lake with hippos, giraffes and zebras grazing in the background, palm trees. Bright sunny day.",
20: "Scene: present-day Colombia: a wide brown river in the remote countryside of the Magdalena region, no city, no buildings, no cars with a large group of wild hippos bathing and grazing on the green riverbank, local fishermen in a small canoe watching from a distance. Lush tropical landscape.",
21: f"Scene: {TEEN}, standing on a street corner of the comuna at dusk; a motorcycle with two men approaches him slowly. Mood of something important coming.",
22: f"Scene: {TEEN}, receiving a set of car keys from a man's hand in front of a shiny new 1980s 4x4 pickup truck with a plain front grille without any badge or lettering parked in a garage; the young man is amazed.",
23: f"Scene: inside the cab of a 1980s 4x4 pickup at night, {TEEN} drives seriously with both hands on the wheel; in the back seat several closed, taped cardboard boxes; city lights through the windshield.",
24: "Scene: a 1980s 4x4 pickup truck driving calmly through the night streets of Medellin, neon-lit shops without words, street lamps, a police checkpoint far in the distance on another street.",
25: "Scene: a large stylized map of the American continent with no text and no labels, glowing golden lines of light spreading from a point in Colombia toward North America and Europe, dark blue background like a war-room table, seen from above, filling the frame, no people, no windows, no signs.",
26: "Scene: aerial view of the endless Colombian Amazon jungle, winding brown rivers, morning mist rising between the trees, a small plane flying far away. Epic and wild.",
27: "Scene: a hidden jungle camp under huge tall trees: wooden huts with roofs covered by camouflage nets and palm leaves, many workers moving around carrying barrels and sacks, generators, a river nearby. No drugs visible.",
28: "Scene: a long red-dirt landing strip cut through the middle of the dense jungle, a small white propeller plane parked at the end, wooden sheds and fuel barrels at the edge.",
29: "Scene: tired, sweaty workers in rubber boots sitting under a palm-leaf shelter during a heavy tropical rainstorm in the jungle camp, mosquitoes, mud everywhere, gloomy mood.",
30: "Scene: several plain dark green 1980s helicopters with no lettering, no words and no markings on them, flying low over the dense jungle canopy toward a hidden camp, dramatic sky, birds fleeing.",
31: "Scene: Colombian police officers in green uniforms walking into the abandoned jungle camp, wooden huts, smoke rising, a captured small plane on the dirt strip. No weapons pointed at anyone.",
32: "Scene: a different jungle camp hidden in another region: on a misty mountain slope covered in jungle, new wooden huts with camouflage roofs being built, workers arriving by boat on a river.",
33: "Scene: a large hangar at a private airfield with several small white and colorful propeller planes (Cessna style) lined up, mechanics working, tropical hills outside.",
34: "Scene: a small propeller plane taking off at night from a hidden dirt strip in the jungle, under a huge full moon, flying very low over the treetops, a few torches marking the runway.",
35: "Scene: a paradise Caribbean island from above: turquoise water, white sand beaches, palm trees, a small landing strip crossing the island with small planes parked, a few villas and boats.",
36: "Scene: inside the cockpit of a small plane flying over the sea, a pilot with aviator sunglasses and mustache counts a thick bundle of green banknotes with a big grin; instruments without numbers.",
37: "Scene: a small propeller plane struggling in a violent thunderstorm over a dark sea at night, lightning bolts, heavy rain, huge clouds. Dramatic.",
38: "Scene: a busy cargo port at dusk with big cargo ships, stacks of colorful shipping containers, cranes, dock workers, a nervous traveler with a suitcase walking to a ship. Containers with no writing.",
39: "Scene: a large glowing globe of the Earth floating in space, golden lines of light connecting Colombia to North America and Europe, and streams of green banknotes flowing back along the lines toward Colombia.",
40: "Scene: a warehouse where workers place huge stacks of green banknote bundles on a gigantic industrial weighing scale like sacks of potatoes, more piles of money all around.",
41: "Scene: a room of a house completely filled with green banknote bundles from floor to ceiling, money also stuffed inside an open wall and under lifted floor tiles; a man looks at it in amazement.",
42: "Scene: a table with a huge mountain of colorful rubber bands next to stacks of banknote bundles each tied with rubber bands, workers sorting them, boxes full of rubber bands.",
43: "Scene: a dark damp basement where several cartoon rats chew and nibble on piles of moldy, wet green banknotes, puddles of water, a single light bulb. Funny but gloomy.",
44: f"Scene: {TEEN}, standing in a dark alley holding a thick bundle of banknotes, looking nervously over his shoulder; shadows of people in the street behind him, tense mood.",
45: "Scene: a wood-paneled judge's office at night; an older judge in a black robe sits at his desk staring at a thick closed envelope left on it; behind him on the wall a huge threatening shadow of a man with a mustache. Tense, ominous.",
46: f"Scene: the grand chamber of the Colombian Congress with rows of seats; {PAB}, wearing a suit and tie this time, stands up while many other congressmen point at him accusingly and turn their backs.",
47: f"Scene: {PAB}, standing in a dim room staring seriously at a large map on the wall (no text, no labels); through the window behind him a big airliner flies away into the sky.",
48: "Scene: Medellin at night seen from a hill, columns of dark smoke rising from the city, red and blue lights of police cars and ambulances, empty streets, a tense and scary mood. No blood, no injured people shown.",
49: f"Scene: {TEEN}, peeking fearfully through the curtains of a dark bedroom window at night; outside, police lights flash on the street and a helicopter searchlight sweeps the houses.",
50: "Scene: a luxurious prison complex on top of a green mountain overlooking Medellin, with white buildings, a football field, watchtowers and a fence, clouds around it. Epic wide view.",
51: f"Scene: luxurious interior of a prison suite with a jacuzzi, a bar, and a big window; {PAB}, stands relaxed by the window looking at the view of the whole city of Medellin far below.",
52: "Scene: several military and police helicopters flying over the dense rooftops of Medellin at dusk, searchlights scanning the streets, soldiers and police vehicles in the streets below. Epic manhunt mood.",
53: "Scene: the red clay-tiled rooftops of a middle-class Medellin neighborhood at sunset, Colombian police officers in uniform on the roofs and in the street below, an orange dramatic sky. No blood, no body shown, no weapons pointed.",
54: "Scene: an abandoned luxurious house, empty and dusty, furniture overturned, a few scattered green banknotes on the floor, drawers open, light coming through dusty windows. Melancholic mood.",
55: "Scene: a melancholic split view: on the left a hillside cemetery with many white crosses under a grey sky above the comuna; on the right an empty prison cell with bars and a small window. Sad, respectful mood.",
56: "Scene: modern present-day Medellin on a bright sunny day: red cable cars (metrocable) gliding over the colorful comuna houses, outdoor escalators with tourists climbing the hillside, colorful murals without words, a modern clean city in the valley.",
57: f"Scene: the poor hillside comuna at sunset like at the beginning; {BOY} looks down from a small window at the glowing city, and far down the steep street a motorcycle with a man in sunglasses is riding up toward his house. Ominous ending.",
}
d = os.path.dirname(os.path.abspath(__file__))
for n, s in S.items():
    open(f"{d}/img{n}.txt", "w").write("MAIN SUBJECT, must be clearly visible, large and in the foreground, this is the most important part of the image: " + s.replace("Scene: ", "") + " " + PRE + POST)
print(len(S), "prompts")
