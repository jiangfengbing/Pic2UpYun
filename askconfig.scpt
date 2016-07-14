#!/usr/bin/osascript

set bucket to the text returned of (display dialog "Bucket?" default answer "" with title "upy-config")
if bucket is not "" then
  set username to the text returned of (display dialog "Username?" default answer "" with title "upy-config")
  if username is not "" then
    set passwd to the text returned of (display dialog "Password?" default answer "" with title "upy-config")
    if passwd is not "" then
      set url_prefix to the text returned of (display dialog "Url Prefix?" default answer "" with title "upy-config")
      if url_prefix is not "" then
        set ret to bucket & "\n" & username & "\n" & passwd & "\n" & url_prefix
        return ret
      end if
    end if
  end if
end if
