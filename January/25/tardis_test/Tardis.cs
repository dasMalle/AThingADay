using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Tardis : MonoBehaviour {
    public static bool inside = false;

    void Update()
    {
        Shader.SetGlobalInt("_Inside", inside ? 1 : 0);
    }
}
