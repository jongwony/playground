using UnityEngine;
using System.Collections;

public class rotate : MonoBehaviour
{
    public Vector3 v;
    public Quaternion q;
    
    // Use this for initialization
    void Start()
    {

        
            // x y z 순서
            transform.FindChild("C1").Rotate(v.x, 0, 0, Space.Self);
            transform.FindChild("C1").Rotate(0, v.y, 0, Space.Self);
            transform.FindChild("C1").Rotate(0, 0, v.z, Space.Self);

            // y x z 순서
            transform.FindChild("C2").Rotate(0, v.y, 0, Space.Self);
            transform.FindChild("C2").Rotate(v.x, 0, 0, Space.Self);
            transform.FindChild("C2").Rotate(0, 0, v.z, Space.Self);

            // z x y 순서
            transform.FindChild("C3").Rotate(0, 0, v.z, Space.Self);
            transform.FindChild("C3").Rotate(v.x, 0, 0, Space.Self);
            transform.FindChild("C3").Rotate(0, v.y, 0, Space.Self);
        

        /*
        // x y z 순서
        transform.FindChild("C1").Rotate(v.x, 0, 0, Space.World);
        transform.FindChild("C1").Rotate(0, v.y, 0, Space.World);
        transform.FindChild("C1").Rotate(0, 0, v.z, Space.World);

        // y x z 순서
        transform.FindChild("C2").Rotate(0, v.y, 0, Space.World);
        transform.FindChild("C2").Rotate(v.x, 0, 0, Space.World);
        transform.FindChild("C2").Rotate(0, 0, v.z, Space.World);

        // z x y 순서
        transform.FindChild("C3").Rotate(0, 0, v.z, Space.World);
        transform.FindChild("C3").Rotate(v.x, 0, 0, Space.World);
        transform.FindChild("C3").Rotate(0, v.y, 0, Space.World);
        */

        // Quaternion Rotation
        //transform.FindChild("Q1").rotation = q;

        // Gimbal Lock
        //transform.FindChild("G1").Rotate(0, 90.0f, 0, Space.Self);

    }

    void FixedUpdate()
    {
        /*
    // x y z 순서
    transform.FindChild("C1").Rotate(Time.deltaTime*v.x, 0, 0, Space.Self);
    transform.FindChild("C1").Rotate(0, Time.deltaTime*v.y, 0, Space.Self);
    transform.FindChild("C1").Rotate(0, 0, Time.deltaTime*v.z, Space.Self);

    // y x z 순서
    transform.FindChild("C2").Rotate(0, Time.deltaTime*v.y, 0, Space.Self);
    transform.FindChild("C2").Rotate(Time.deltaTime*v.x, 0, 0, Space.Self);
    transform.FindChild("C2").Rotate(0, 0, Time.deltaTime*v.z, Space.Self);

    // z x y 순서
    transform.FindChild("C3").Rotate(0, 0, Time.deltaTime*v.z, Space.Self);
    transform.FindChild("C3").Rotate(Time.deltaTime*v.x, 0, 0, Space.Self);
    transform.FindChild("C3").Rotate(0, Time.deltaTime*v.y, 0, Space.Self);
*/

/*
        // x y z 순서
        transform.FindChild("C1").Rotate(Time.deltaTime*v.x, 0, 0, Space.World);
        transform.FindChild("C1").Rotate(0, Time.deltaTime*v.y, 0, Space.World);
        transform.FindChild("C1").Rotate(0, 0, Time.deltaTime*v.z, Space.World);

        // y x z 순서
        transform.FindChild("C2").Rotate(0, Time.deltaTime*v.y, 0, Space.World);
        transform.FindChild("C2").Rotate(Time.deltaTime*v.x, 0, 0, Space.World);
        transform.FindChild("C2").Rotate(0, 0, Time.deltaTime*v.z, Space.World);

        // z x y 순서
        transform.FindChild("C3").Rotate(0, 0, Time.deltaTime*v.z, Space.World);
        transform.FindChild("C3").Rotate(Time.deltaTime*v.x, 0, 0, Space.World);
        transform.FindChild("C3").Rotate(0, Time.deltaTime*v.y, 0, Space.World);
*/

        // Quaternion Rotation
        Debug.Log("w=" + transform.FindChild("Q1").rotation.w + "x=" + transform.FindChild("Q1").rotation.x + "y=" + transform.FindChild("Q1").rotation.y + "z=" + transform.FindChild("Q1").rotation.z);


        // Gimbal Lock
        transform.FindChild("G1").Rotate(0, 90.0f, 0, Space.Self);
        transform.FindChild("G1").Rotate(Time.deltaTime  * 30.0f, 0, 0 ,Space.Self);
        transform.FindChild("G1").Rotate(0, 0, Time.deltaTime * 30.0f,Space.Self);

    }
}
