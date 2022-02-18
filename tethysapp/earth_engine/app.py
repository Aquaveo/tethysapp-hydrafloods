from tethys_sdk.base import TethysAppBase, url_map_maker


class EarthEngine(TethysAppBase):
    """
    Tethys app class for Earth Engine.
    """

    name = 'Earth Engine'
    index = 'earth_engine:home'
    icon = 'earth_engine/images/earth-engine-logo.png'
    package = 'earth_engine'
    root_url = 'earth-engine'
    color = '#84ADEA'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='earth-engine',
                controller='earth_engine.controllers.home'
            ),
            UrlMap(
                name='get_image_collection',
                url='earth-engine/get-image-collection',
                controller='earth_engine.controllers.get_image_collection'
            ),
            UrlMap(
                name='get_image_layer',
                url='get-image-layer/',
                controller='earth_engine.controllers.retrieve_layer'
            ),
            UrlMap(
                name='get_export',
                url='get-export/',
                controller='earth_engine.controllers.export_layer'
            )

        )

        return url_maps
