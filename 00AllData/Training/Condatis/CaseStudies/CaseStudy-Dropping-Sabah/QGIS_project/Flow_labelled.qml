<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.18.17" minimumScale="inf" maximumScale="1e+08" hasScaleBasedVisibilityFlag="0">
  <pipe>
    <rasterrenderer opacity="1" alphaBand="-1" classificationMax="1.164" classificationMinMaxOrigin="User" band="1" classificationMin="0" type="singlebandpseudocolor">
      <rasterTransparency/>
      <rastershader>
        <colorrampshader colorRampType="DISCRETE" clip="0">
          <item alpha="0" value="0" label="&lt;= 0" color="#fcffa4"/>
          <item alpha="255" value="0.388" label="Low flow" color="#fca40b"/>
          <item alpha="255" value="0.582" label=" " color="#dd5039"/>
          <item alpha="255" value="0.776" label="Medium flow" color="#932567"/>
          <item alpha="255" value="0.97" label=" " color="#420a68"/>
          <item alpha="255" value="inf" label="High flow" color="#000004"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeGreen="128" colorizeOn="0" colorizeRed="255" colorizeBlue="128" grayscaleMode="0" saturation="0" colorizeStrength="100"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
