using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Camera))]
public class RTCamera : MonoBehaviour {
    public Shader replacementShader;

    internal RenderTexture rt;
    internal Camera cam;

	// Use this for initialization
	void Start () {
        cam = GetComponent<Camera>();

        rt = new RenderTexture(Screen.width, Screen.height, 24, RenderTextureFormat.Default);
        rt.Create();

        cam.targetTexture = rt;

        if ( replacementShader != null ) {
            cam.SetReplacementShader(replacementShader, null);
        }
	}
}
