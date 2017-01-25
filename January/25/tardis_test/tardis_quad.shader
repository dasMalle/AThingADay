Shader "tardis_quad"
{
	Properties
	{
		_Color("Color",Color) = (1,0,0,1)
		_World("Texture", 2D) = "white" {}
		_Tardis("Texture", 2D) = "white" {}
		_Mask("Texture", 2D) = "black" {}
	}
	SubShader
	{
		// No culling or depth
		Cull Off ZWrite Off ZTest Always
		
		Pass
		{
			CGPROGRAM
			#pragma vertex vert
			#pragma fragment frag
			
			#include "UnityCG.cginc"

			struct appdata
			{
				float4 vertex : POSITION;
				float2 uv : TEXCOORD0;
			};

			struct v2f
			{
				float2 uv : TEXCOORD0;
				float4 vertex : SV_POSITION;
			};

			v2f vert (appdata v)
			{
				v2f o;
				o.vertex = mul(UNITY_MATRIX_MVP, v.vertex);
				o.uv = ComputeScreenPos(o.vertex);
				return o;
			}
			
			sampler2D _Tardis;
			sampler2D _World;
			sampler2D _Mask;
			uniform sampler2D _LastCameraDepthTexture;
			uniform int _Inside;

			fixed4 frag (v2f i) : SV_Target
			{
				fixed4 col1 = tex2D(_World, i.uv);
				fixed4 col2 = tex2D(_Tardis, i.uv);
				fixed mask = tex2D(_Mask, i.uv).r;

				if (_Inside) {
					return lerp(col2, col1, mask);
				}
				else {
					return lerp(col1, col2, mask);
				}
			}
			ENDCG
		}
		
	}
}
