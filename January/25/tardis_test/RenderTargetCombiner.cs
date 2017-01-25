using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RenderTargetCombiner : MonoBehaviour {
    public RTCamera normal, tardis, mask;
    public Material combiner;

    void OnPostRender() {
        combiner.SetTexture("_World", normal.rt);
        combiner.SetTexture("_Tardis", tardis.rt);
        combiner.SetTexture("_Mask", mask.rt);
    }
}