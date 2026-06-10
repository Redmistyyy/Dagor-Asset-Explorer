
from util.terminable import Exportable
from collections import OrderedDict

class AssetCacher:
	"""Global asset cache with per-class capacity limits and model-name index."""

	MAX_PER_CLASS = 500      # max cached assets per type
	__cachedAssets = {}      # {type: OrderedDict{name: [asset, ...]}}
	__modelsDesc = {}        # {filePath: desc}
	__modelIndex = {}        # {model_name: [desc, ...]}  — reverse index for O(1) lookup

	@classmethod
	def cacheAsset(cls, asset: Exportable):
		assetClass = type(asset)

		if assetClass not in cls.__cachedAssets:
			cls.__cachedAssets[assetClass] = OrderedDict()

		classCache: OrderedDict = cls.__cachedAssets[assetClass]
		name = asset.name

		if name not in classCache:
			classCache[name] = []
		classCache[name].append(asset)

		# evict oldest if over limit
		while len(classCache) > cls.MAX_PER_CLASS:
			classCache.popitem(last=False)

	@classmethod
	def uncacheAsset(cls, asset: Exportable):
		if asset in cls.__modelsDesc.values():
			del cls.__modelsDesc[asset.filePath]
			return

		assetClass = type(asset)
		if assetClass not in cls.__cachedAssets:
			return

		classCache = cls.__cachedAssets[assetClass]
		name = asset.name
		if name not in classCache:
			return

		classCache[name].remove(asset)
		if not classCache[name]:
			del classCache[name]

	@classmethod
	def clearCache(cls, assetClass: type[Exportable] = None):
		if assetClass is None:
			cls.__modelsDesc.clear()
			cls.__modelIndex.clear()
			cls.__cachedAssets.clear()
		elif assetClass in cls.__cachedAssets:
			del cls.__cachedAssets[assetClass]

	@classmethod
	def getAssetCache(cls, assetClass: type[Exportable] = None):
		if assetClass is None:
			return cls.__cachedAssets
		return cls.__cachedAssets.get(assetClass, {})

	@classmethod
	def getCachedAsset(cls, assetClass: type[Exportable], name: str) -> list:
		classCache = cls.__cachedAssets.get(assetClass)
		if classCache is None:
			return False
		return classCache.get(name, False)

	@classmethod
	def isCached(cls, asset: Exportable):
		classCache = cls.__cachedAssets.get(type(asset))
		if classCache is None:
			return False
		return asset in classCache.get(asset.name, [])

	@classmethod
	def appendGameResDesc(cls, desc):
		cls.__modelsDesc[desc.filePath] = desc

	@classmethod
	def _findDescForModel(cls, model: str):
		"""Find the first GameResDesc that contains the given model name. Results are cached."""
		if model in cls.__modelIndex:
			return cls.__modelIndex[model]
		for desc in cls.__modelsDesc.values():
			if desc.hasName(model):
				cls.__modelIndex[model] = desc
				return desc
		cls.__modelIndex[model] = None  # negative cache
		return None

	@classmethod
	def getModelTextures(cls, model: str) -> list[str]:
		desc = cls._findDescForModel(model)
		return desc.getModelTextures(model) if desc else []

	@classmethod
	def getModelMaterials(cls, model: str) -> list[str]:
		desc = cls._findDescForModel(model)
		return desc.getModelMaterials(model) if desc else []

	@classmethod
	def getSkinnedMaterials(cls, model: str) -> list[str]:
		desc = cls._findDescForModel(model)
		return desc.getSkinnedMaterials(model) if desc else []
