import os
import wx
import pcbnew
import inspect


def get_path():
    # Get the script directory in order to locate icons.
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    return os.path.dirname(os.path.abspath(filename))


if __name__ == "__main__":
    app = wx.App()
