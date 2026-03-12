# -*- coding: utf-8 -*-
"""
BeatUp 8-Row Convert Tool - CLI Version
Created on Thu 12/03/2026

@author: Wilson & Trương Kỳ Anh QN

Usage:
    python BeatUp8row_cli.py
"""
import os
from base64 import b64decode

# Base64 encoded string for SLK file content
BASE_SLK = "SUQ7UFdYTDtOO0UNClA7UEdlbmVyYWwNClA7UDANClA7UDAuMDANClA7UCMsIyMwDQpQO1AjLCMjMC4wMA0KUDtQIywjIzBfKTs7XCgjLCMjMFwpDQpQO1AjLCMjMF8pOztbUmVkXVwoIywjIzBcKQ0KUDtQIywjIzAuMDBfKTs7XCgjLCMjMC4wMFwpDQpQO1AjLCMjMC4wMF8pOztbUmVkXVwoIywjIzAuMDBcKQ0KUDtQIiQiIywjIzBfKTs7XCgiJCIjLCMjMFwpDQpQO1AiJCIjLCMjMF8pOztbUmVkXVwoIiQiIywjIzBcKQ0KUDtQIiQiIywjIzAuMDBfKTs7XCgiJCIjLCMjMC4wMFwpDQpQO1AiJCIjLCMjMC4wMF8pOztbUmVkXVwoIiQiIywjIzAuMDBcKQ0KUDtQMCUNClA7UDAuMDAlDQpQO1AwLjAwRSswMA0KUDtQIyMwLjBFKzANClA7UCNcID8vPw0KUDtQI1wgPz8vPz8NClA7UG0vZC95eXl5DQpQO1BkXC1tbW1cLXl5DQpQO1BkXC1tbW0NClA7UG1tbVwteXkNClA7UGg6bW1cIEFNL1BNDQpQO1BoOm1tOnNzXCBBTS9QTQ0KUDtQaDptbQ0KUDtQaDptbTpzcw0KUDtQbS9kL3l5eXlcIGg6bW0NClA7UG1tOnNzDQpQO1BtbTpzcy4wDQpQO1BADQpQO1BbaF06bW06c3MNClA7UF8oIiQiKiAjLCMjMF8pOztfKCIkIiogXCgjLCMjMFwpOztfKCIkIiogIi0iXyk7O18oQF8pDQpQO1BfKCogIywjIzBfKTs7XygqIFwoIywjIzBcKTs7XygqICItIl8pOztfKEBfKQ0KUDtQXygiJCIqICMsIyMwLjAwXyk7O18oIiQiKiBcKCMsIyMwLjAwXCk7O18oIiQiKiAiLSI/P18pOztfKEBfKQ0KUDtQXygqICMsIyMwLjAwXyk7O18oKiBcKCMsIyMwLjAwXCk7O18oKiAiLSI/P18pOztfKEBfKQ0KUDtGQ2FsaWJyaTtNMjIwO0w5DQpQO0ZDYWxpYnJpO00yMjA7TDkNClA7RkNhbGlicmk7TTIyMDtMOQ0KUDtGQ2FsaWJyaTtNMjIwO0w5DQpQO0VDYWxpYnJpO00yMjA7TDkNClA7RUNhbGlicmkgTGlnaHQ7TTM2MDtMNTUNClA7RUNhbGlicmk7TTMwMDtTQjtMNTUNClA7RUNhbGlicmk7TTI2MDtTQjtMNTUNClA7RUNhbGlicmk7TTIyMDtTQjtMNTUNClA7RUNhbGlicmk7TTIyMDtMMTgNClA7RUNhbGlicmk7TTIyMDtMMjENClA7RUNhbGlicmk7TTIyMDtMNjENClA7RUNhbGlicmk7TTIyMDtMNjMNClA7RUNhbGlicmk7TTIyMDtTQjtMNjQNClA7RUNhbGlicmk7TTIyMDtTQjtMNTMNClA7RUNhbGlicmk7TTIyMDtMNTMNClA7RUNhbGlicmk7TTIyMDtTQjtMMTANClA7RUNhbGlicmk7TTIyMDtMMTENClA7RUNhbGlicmk7TTIyMDtTSTtMMjQNClA7RUNhbGlicmk7TTIyMDtTQjtMOQ0KUDtFQ2FsaWJyaTtNMjIwO0wxMA0KUDtFU2Vnb2UgVUk7TTIwMDtMOQ0KRjtQMDtERzBHODtNMzAwDQpCO1kxNjIwO1g2O0QwIDAgMTYxOSA1DQpPO0Q7VjA7SzQ3O1QwO0cxMDAgMC4wMDENCkM7WTE7WDE7SyJNZWFzdXJlIg0KQztYMjtLIjEvNCINCkM7WDM7SyIxLzE2Ig0KQztYNDtLIkxvY2F0aW9uIg0KQztYNTtLIlR5cGUiDQpDO1g2O0siS2V5Ig0KQztZMjtYMTtLImludCINCkM7WDI7SyJpbnQiDQpDO1gzO0siaW50Ig0KQztYNDtLImludCINCkM7WDU7SyJlbnVtKG4scyxmKSINCkM7WDY7SyJzdHJpbmciDQo="
SLK_HEADER = b64decode(BASE_SLK)


def read_file(path):
    """Read file with encoding fallback."""
    for enc in ['utf-8-sig', 'utf-8', 'cp1252', 'latin-1']:
        try:
            with open(path, "r", encoding=enc) as f:
                return f.readlines()
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Cannot read file: {path}")


# ─── SM → SLK ────────────────────────────────────────────────────────────────

def sm_to_slk(path):
    lines = read_file(path)

    # Extract note rows — only accept lines where all chars are 0-3 (or inline , / ;)
    in_notes = False
    notes_lines = []
    for line in lines:
        if "#NOTES:" in line:
            in_notes = True
            continue
        if not in_notes:
            continue
        s = line.replace("\n", "").replace("\r", "").strip()
        if not s:
            continue
        if s in (",", ";"):
            notes_lines.append(s)
            continue
        has_sep = s.endswith(",") or s.endswith(";")
        core = s[:-1] if has_sep else s
        if core and all(c in "0123" for c in core):
            notes_lines.append(s)

    # Split into madis (measures)
    madi_section = []
    madis = []
    for note in notes_lines:
        if note == ";":
            madis.append(madi_section)
            madi_section = []
            break
        elif note == ",":
            madis.append(madi_section)
            madi_section = []
        elif note.endswith(","):
            actual = note[:-1]
            if actual:
                madi_section.append(actual)
            madis.append(madi_section)
            madi_section = []
        elif note.endswith(";"):
            actual = note[:-1]
            if actual:
                madi_section.append(actual)
            madis.append(madi_section)
            madi_section = []
            break
        else:
            madi_section.append(note)

    resolution = 4
    note_location = [0, 0, 0]
    enum_dict = {6: "s", 7: "f"}
    key_dict = {0: "7", 1: "4", 2: "1", 3: "9", 4: "6", 5: "3"}
    data = []

    for madi in madis:
        num_rows = len(madi)
        note_increment = int(resolution / (num_rows / 4)) if num_rows > 0 else 0

        for row_note in madi:
            if "1" in row_note:
                note_num = (note_location[0] * 16) + (note_location[1] * 4) + note_location[2]
                found_enums = []
                found_keys = []
                has_normal = False
                for i in range(len(row_note)):
                    if row_note[i] == "1":
                        if i in enum_dict:
                            found_enums.append(enum_dict[i])
                        elif 0 <= i <= 5:
                            has_normal = True
                        key_val = key_dict.get(i)
                        if key_val:
                            found_keys.append(key_val)
                if has_normal:
                    found_enums.insert(0, "n")
                if found_enums or found_keys:
                    final_enum = ",".join(found_enums)
                    final_key = found_keys[0] if found_keys else ""
                    data.append([note_location[0], note_location[1], note_location[2],
                                 note_num, final_enum, final_key])

            note_location[2] += note_increment
            if note_location[2] >= resolution:
                note_location[2] = 0
                note_location[1] += 1
            if note_location[1] >= 4:
                note_location[1] = 0
                note_location[0] += 1

    sm_name = os.path.splitext(os.path.basename(path))[0]
    out_path = os.path.join(os.path.dirname(path), f"BU_{sm_name}.slk")
    row_c = 3
    with open(out_path, "wb") as f:
        f.write(SLK_HEADER)
        for row in data:
            store_value = f"C;Y{row_c};"
            for i, val in enumerate(row):
                if i >= 4:
                    store_value += f'X{i+1};K"{val}"\r\n'
                else:
                    store_value += f'X{i+1};K{val}\r\n'
                f.write(bytes(store_value, "utf-8"))
                store_value = "C;"
            row_c += 1
        f.write(bytes("E\r\n", "utf-8"))

    print(f"  [OK] Saved: {out_path}")


# ─── SLK → SM ────────────────────────────────────────────────────────────────

def slk_to_sm(path, music_file, bpm):
    lines = read_file(path)

    y_groups = {}
    current_y = None
    for line in lines:
        if not line.startswith("C;"):
            continue
        parts = line.strip().split(";")
        row_data = {}
        for p in parts[1:]:
            if not p:
                continue
            k = p[0]
            v = p[1:]
            row_data[k] = v
        if "Y" in row_data:
            current_y = int(row_data["Y"])
            if current_y not in y_groups:
                y_groups[current_y] = {}
        if current_y is not None and "X" in row_data:
            val = row_data.get("K", "").strip('"')
            y_groups[current_y][int(row_data["X"])] = val

    notes_extracted = []
    for y in sorted(y_groups.keys()):
        if y < 3:
            continue
        row = y_groups[y]
        try:
            notes_extracted.append({
                "measure": int(row.get(1, 0)),
                "beat":    int(row.get(2, 0)),
                "tick":    int(row.get(3, 0)),
                "type":    row.get(5, ""),
                "key":     row.get(6, "")
            })
        except Exception:
            continue

    max_m = max(n["measure"] for n in notes_extracted) if notes_extracted else 0
    resolution = 16
    measures_data = {}

    for n in notes_extracted:
        m = n["measure"]
        if m not in measures_data:
            measures_data[m] = [["0"] * 8 for _ in range(resolution)]
        row_idx = (n["beat"] * 4) + n["tick"]
        if row_idx < resolution:
            key_map = {"7": 0, "4": 1, "1": 2, "9": 3, "6": 4, "3": 5}
            if n["key"] in key_map:
                measures_data[m][row_idx][key_map[n["key"]]] = "1"
            for t in n["type"].split(","):
                if t == "s":
                    measures_data[m][row_idx][6] = "1"
                elif t == "f":
                    measures_data[m][row_idx][7] = "1"

    header = f"""#TITLE:BUConverterByKyAnh;
#MUSIC:{music_file};
#OFFSET:0.000;
#BPMS:0.000={bpm};
//--------------- dance-double -  ----------------
#NOTES:
     dance-double:
     :
     Beginner:
     1:
     0,0,0,0,0:
"""
    body = []
    for i in range(max_m + 1):
        m_data = measures_data.get(i, [["0"] * 8 for _ in range(resolution)])
        body.append("\n".join(["".join(r) for r in m_data]))

    out_content = header + "\n,\n".join(body) + "\n;"

    base_name = os.path.splitext(os.path.basename(path))[0]
    if base_name.startswith("BU_"):
        base_name = base_name[3:]
    out_path = os.path.join(os.path.dirname(path), f"SM_{base_name}.sm")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out_content)

    print(f"  [OK] Saved: {out_path}")


# ─── Main ─────────────────────────────────────────────────────────────────────

def list_files(directory, ext):
    return [f for f in os.listdir(directory) if f.lower().endswith(ext)]


def main():
    print("=" * 50)
    print("  Audition Beat-Up 8-Row Convert Tool (CLI)")
    print("  by Wilson & Trương Kỳ Anh QN")
    print("=" * 50)

    cwd = os.path.dirname(os.path.abspath(__file__))

    sm_files  = list_files(cwd, ".sm")
    slk_files = list_files(cwd, ".slk")

    all_files = [(f, "sm")  for f in sm_files] + \
                [(f, "slk") for f in slk_files]

    if not all_files:
        print("No .sm or .slk files found in the current directory.")
        return

    print("\nAvailable files:")
    for i, (name, ftype) in enumerate(all_files):
        print(f"  [{i+1}] {name}  ({ftype.upper()} → {'SLK' if ftype=='sm' else 'SM'})")

    try:
        choice = int(input("\nChoose file number: ")) - 1
        filename, ftype = all_files[choice]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    path = os.path.join(cwd, filename)

    print(f"\nSelected: {filename}")
    print(f"Mode: {'SM → SLK' if ftype == 'sm' else 'SLK → SM'}")

    try:
        if ftype == "sm":
            sm_to_slk(path)
        else:
            music_file = input("Music filename (e.g., song.ogg): ").strip()
            base = os.path.splitext(filename)[0]
            if not music_file:
                music_file = f"{base[3:] if base.startswith('BU_') else base}.ogg"
                print(f"  Auto-filled: {music_file}")
            bpm = input("BPM (e.g., 150): ").strip() or "150"
            slk_to_sm(path, music_file, bpm)
    except Exception as e:
        print(f"  [ERROR] {e}")
        return

    print("\nDone!")
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
