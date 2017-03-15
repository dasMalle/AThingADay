Shader "tardis_mask"
{
	Properties { }
	SubShader
	{
		Pass
		{
			Cull back

			CGPROGRAM
			#pragma vertex vert
			#pragma fragment frag

			#include "UnityCG.cginc"
				struct appdata
				{
					float4 vertex : POSITION;
				};

				struct v2f
				{
					float4 vertex : SV_POSITION;
				};

				v2f vert(appdata v)
				{
					v2f o;
					o.vertex = mul(UNITY_MATRIX_MVP, v.vertex);
					return o;
				}

				uniform sampler2D _CameraDepthTexture;

				fixed4 frag(v2f i) : SV_Target
				{
					float2 fragmentScreenCoordinates = float2(i.vertex.x / _ScreenParams.x, i.vertex.y / _ScreenParams.y);
					float sceneDepthSample = tex2D(_CameraDepthTexture, fragmentScreenCoordinates).x;
					bool culled = (sceneDepthSample < i.vertex.z);

					return culled ? 1 : 0;
				}
			ENDCG
		}
	}
}
