# fman modules
from fman import DirectoryPaneCommand, show_alert, show_status_message
from fman.url import as_human_readable, as_url, dirname
from fman.fs import exists, is_dir
# python modules
import re # for regular expression
import os # for os and processes

# main program
class GotoShortcutTarget(DirectoryPaneCommand):
    def __call__(self):
        # check file under cursor
        current_file = self.pane.get_file_under_cursor()
        # simply checking the file extension
        if re.compile( r'\.lnk$').search(current_file):
            # ok, let's receive the real folder containing the target of that shortcut
            shellscript = os.path.dirname(__file__) + "\link_target.ps1 "
            command = "powershell -ExecutionPolicy Bypass -NoLogo -Noninteractive -noprofile"
            command += ' -file "' + shellscript + '"'
            command += ' -link "' + as_human_readable(current_file) + '"'
            #show_status_message("Command: " + command) # temporary
            target = as_url(os.popen(command).read().strip())
            show_status_message("Target: " + target, 2)

            # what did we get?
            if False == exists(target):
                # target is not reachable...
                show_alert(target + " doesn't exist.")
            elif is_dir(target):
                # target is a folder, we go to it
                self.pane.set_path(target)
            else:
                # target is a file, we go to its directory
                self.pane.set_path( dirname(target) )
        else:
            # nope, wrong thing
            show_alert(current_file + " is not a shortcut.")
