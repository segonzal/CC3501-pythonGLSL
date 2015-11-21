#version 120
varying vec4 myColor;
varying vec3 myNormal;
varying vec3 myPosition;

uniform vec3 lightPos;
uniform vec3 lightCol;

void main(){
  float d = max(dot(myNormal,normalize(lightPos-myPosition)),0.0);
	float blend = 0.5;
	vec3 color = blend*(lightCol*d) + (1-blend)*myColor.rgb;
	gl_FragColor = vec4(color,myColor.a);
}
