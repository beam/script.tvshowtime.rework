import os
import xbmc, xbmcaddon
import time
import json

__addon__         = xbmcaddon.Addon()
__cwd__           = __addon__.getAddonInfo('path')
__scriptname__    = __addon__.getAddonInfo('name')
__version__       = __addon__.getAddonInfo('version')
__language__      = __addon__.getLocalizedString
__resource_path__ = os.path.join(__cwd__, 'resources', 'lib')
__resource__      = xbmc.translatePath(__resource_path__).decode('utf-8')

sys.path.append (__resource__)

from utilities import log, get_episode_info

class KodiMonitor(xbmc.Monitor):

    def onNotification(self, sender, method, data):
    	if method == "VideoLibrary.OnUpdate" or method == 'Player.OnStop':
    		parsed_data = json.loads(data)
    		log(parsed_data)
    		if parsed_data['item']['type'] == 'episode':
    			episode_id = parsed_data['item']['id']
    			tvdb_data = get_episode_info(episode_id)
    			log(str(tvdb_data))


if (__name__ == "__main__"):
    log("Starting.. " + __version__)
    monitor = KodiMonitor()
    while not monitor.abortRequested():
	    if monitor.waitForAbort(10): break
    del monitor
    log("Stopped.. " + __version__)
