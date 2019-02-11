# WinShortcutTarget
Open folder containing the target of a shortcut under Windows.

- default binding: F3
- action name: Goto Shortcut Target

I had this idea at work because I often need to open folders containing the files I have shortcuts on my desktop.

This plugin simply follows windows shortcuts and opens the folder containing the target of the shortcut.

It the shortcut is a folder, it'll open the folder normally (in that case you might prefer the default action).  
If it's a file, it'll open the folder containing the file. 

To find the shortcut target I use a powershell script.  
Launching powershell takes a little second, so the preformances are not great (at least on my computer).

If you have ideas on how to improve that plugin, don't hesitate to open an issue.
