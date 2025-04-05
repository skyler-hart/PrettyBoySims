import os
import sims4.log
import sims4.commands

@sims4.commands.Command('ghostshell.hello', command_type=sims4.commands.CommandType.Live)
def ghostshell_hello(_connection=None):
    sims4.commands.output("👻 Hello from GhostShell", _connection)

    try:
        path = os.path.expanduser("~/Documents/Electronic Arts/The Sims 4/GhostShell.txt")
        with open(path, "a", encoding="utf-8") as f:
            f.write("👻 Hello from GhostShell cheat\\n")
    except Exception as e:
        sims4.commands.output(f"❌ Log failed: {e}", _connection)
