import importlib
import os


class Plugins:
    def __init__(self):
        self.pluginFile = []  # 存储插件文件名称
        self.pluginFunction = []  # 存储插件函数
        pass

    def listPlugins(self):
        for pluginName in os.listdir("./plugins/"):
            if not pluginName.startswith("_") and os.path.isdir("./plugins/" + str(pluginName)):
                self.pluginFile.append(str(pluginName))

    def loadPlugins(self):
        print(self.pluginFile)
        for pluginName in self.pluginFile:
            self.pluginFunction.append(importlib.import_module("plugins." + pluginName + ".main"))
        return self.pluginFunction
        pass

    def initPlugins(self, filename: str):
        pluginsPath = os.path.splitext(filename)[0]
        print(pluginsPath)


if __name__ == '__main__':
    p = Plugins()
    p.listPlugins()
    for loadPlugins in p.loadPlugins():
        loadPlugins.OnLoad()
