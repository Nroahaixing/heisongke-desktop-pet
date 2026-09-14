import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")

def load_frames(state, count):
    return [f"../assets/{state}/{state}_{i}.png" for i in range(1, count + 1)]

data = {
    "normal": load_frames("normal", 9),
    "levelup": load_frames("levelup", 16),
    "wave": load_frames("wave", 12),
    "idea": load_frames("idea", 12),
    "followup": load_frames("followup", 16),
    "crosslink": load_frames("crosslink", 16),
    "savecard": load_frames("savecard", 18),
    "mastered": load_frames("mastered", 16),
    "forgotten": load_frames("forgotten", 16),
    "newnote": load_frames("newnote", 16),
    "newbook": load_frames("newbook", 15),
}

frames_json = json.dumps(data)

template_path = os.path.join(HERE, "demo_template.html")
html_template = open(template_path, encoding="utf-8").read()
out = html_template.replace("__FRAMES_JSON__", frames_json)

out_path = os.path.join(HERE, "pet_demo.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(out)

print("wrote", out_path, "size(bytes)=", os.path.getsize(out_path))
