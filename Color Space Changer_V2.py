import maya.cmds as cmds

def apply_color_space_to_selected(target_color_space):
    sel = cmds.ls(selection=True)

    if not sel:
        cmds.warning("No nodes selected.")
        return

    for node in sel:
        if cmds.nodeType(node) == "file":
            if cmds.attributeQuery("colorSpace", node=node, exists=True):
                cmds.setAttr(node + ".colorSpace", target_color_space, type="string")
                print("Set {}.colorSpace to {}".format(node, target_color_space))
            else:
                print("{} has no colorSpace attribute.".format(node))
        else:
            print("{} is not a file node.".format(node))

def show_color_space_changer():
    win_name = "colorSpaceChangerWin"
    if cmds.window(win_name, exists=True):
        cmds.deleteUI(win_name)

    # Let Maya auto-size the window
    cmds.window(win_name, title="Color Space Changer", sizeable=False)

    cmds.columnLayout(adjustableColumn=True, rowSpacing=10, columnAlign="center")

    cmds.text(label="Select Color Space:")
    cmds.optionMenu("colorSpaceOption", width=250)
    cmds.menuItem(label="ACES - ACEScg")
    cmds.menuItem(label="srgb_texture")
    cmds.menuItem(label="out_srgb")
    cmds.menuItem(label="lin_srgb")
    cmds.menuItem(label="Utility - sRGB - Texture")
    cmds.menuItem(label="Utility - Linear - sRGB")
    cmds.menuItem(label="Output - sRGB")
    cmds.menuItem(label="raw")


    cmds.button(label="Apply to Selected File Nodes", width=250, height=30, command=lambda x: on_apply())

    cmds.showWindow(win_name)

def on_apply():
    selected_color_space = cmds.optionMenu("colorSpaceOption", query=True, value=True)
    apply_color_space_to_selected(selected_color_space)

# Run the tool
show_color_space_changer()
