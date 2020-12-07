1# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# ------------ LOAD HOLOPLAY CORE WRAPPER ---------------
# CLASS USED FOR THE IMPORTANT GLOBAL VARIABLES AND LISTS IN THIS ADDON
class LookingGlassAddon:

	# path to the addon directory
	path = None

	# Was the connection to the holoplay service successfully initialized?
	HoloPlayService = False

	# List of dictionaries with one dictionary for each connected Looking Glass
	# Each Dictionary contains all available data on the Looking Glass (including calibrations data)
	deviceList = []

	# Was the modal operator for the frustum initialized?
	FrustumInitialized = False

	# Was the modal operator for the 3D cursor initialized?
	CursorInitialized = True

	# The Window object representing the Blender main window and the Space object, which are used for the lightfield rendering
	lightfieldWindow = None
	lightfieldRegion = None
	lightfieldArea = None
	lightfieldSpace = None

	# The active Window and Viewport the user is currently working in
	BlenderWindow = None
	BlenderViewport = None


	# SHADER SOURCES
	# +++++++++++++++++++++++++++++++++++++++
	lightfieldVertexShaderSource = None
	lightfieldFragmentShaderSource = None



	# GLOBAL LIST OF QUILT Settings
	# +++++++++++++++++++++++++++++++++++++++
	# define a list
	qs = []

	# set up quilt settings
	def setupQuiltPresets():

		# there are 3 presets to choose from:
		# - standard settings
		LookingGlassAddon.qs.append({
				"width": 2048,
				"height": 2048,
				"columns": 4,
				"rows": 8,
				"totalViews": 32,
				"quiltOffscreen": None,
				"viewOffscreens": []
				})

		# - high resolution settings (4k)
		LookingGlassAddon.qs.append({
				"width": 4095,
				"height": 4095,
				"columns": 5,
				"rows": 9,
				"totalViews": 45,
				"quiltOffscreen": None,
				"viewOffscreens": []
				})

		# - 8k settings
		LookingGlassAddon.qs.append({
				"width": 4096 * 2,
				"height": 4096 * 2,
				"columns": 5,
				"rows": 9,
				"totalViews": 45,
				"quiltOffscreen": None,
				"viewOffscreens": []
				})

		# - LOW RESOLUTION FOR PREVIEW
		LookingGlassAddon.qs.append({
				"width": 512,
				"height": 512,
				"columns": 4,
				"rows": 8,
				"totalViews": 32,
				"quiltOffscreen": None,
				"viewOffscreens": []
				})

		# iterate through all presets
		for i in range(0, len(LookingGlassAddon.qs), 1):

			# calculate viewWidth and viewHeight
			LookingGlassAddon.qs[i]["viewWidth"] = int(round(LookingGlassAddon.qs[i]["width"] / LookingGlassAddon.qs[i]["columns"]))
			LookingGlassAddon.qs[i]["viewHeight"] = int(round(LookingGlassAddon.qs[i]["height"] / LookingGlassAddon.qs[i]["rows"]))
