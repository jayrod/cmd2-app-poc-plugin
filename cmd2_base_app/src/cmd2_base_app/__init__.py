""" Entry point of cmd2 application """
from cmd2_base_app.app import App

import pluginlib


def main():

    #load plugins
    loader = pluginlib.PluginLoader(entry_point='cmd2_plugins')
    plugins = loader.plugins

    if 'CommandSets' not in plugins.keys():
        my_sets = []
    else:
        my_sets = [o() for o in plugins.CommandSets.values()]

    c = App(command_sets=my_sets)
    c.cmdloop()
