__author__ = 'mllorens'

VERTEX = """

attribute vec3 position;
attribute vec4 color;
attribute vec3 normal;

varying vec4 myColor;
varying vec3 myNormal;
varying vec3 myPosition;

uniform vec3 lightPos;

void main(){
	myColor = color;
	myNormal = normal;
	myPosition = position;
	gl_Position = gl_ModelViewProjectionMatrix * vec4(myPosition,1.0);
}
"""

FRAGMENT = """

varying vec4 myColor;
varying vec3 myNormal;
varying vec3 myPosition;

uniform vec3 lightPos;
uniform vec3 lightCol;

void main(){
    float blend = 0.5;
    float d = max(dot(myNormal,normalize(lightPos-myPosition)),0.0);
    vec3 color = blend*lightCol + (1-blend)*myColor;
	gl_FragColor = vec4(color*d,myColor.a);
}
"""