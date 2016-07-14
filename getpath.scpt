#!/usr/bin/osascript

activate application "SystemUIServer"
tell application "Finder"
  activate
  return get POSIX path of (get selection as «class furl»)
end tell
