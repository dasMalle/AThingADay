using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Exit : MonoBehaviour {
	void OnTriggerExit( Collider other)
    {
        if ( Tardis.inside )
        {
            Tardis.inside = false;
        }
    }
}
