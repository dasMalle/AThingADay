using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Entrance : MonoBehaviour {

	void OnTriggerEnter( Collider other )
    {
        if (!Tardis.inside)
        {
            Tardis.inside = true;
        }
    }
}
