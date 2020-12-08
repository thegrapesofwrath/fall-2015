/**
 * Mandelbulber v2, a 3D fractal generator
 *
 * cOneParameter class - stores all information of one parameter
 *
 * Copyright (C) 2014 Krzysztof Marczak
 *
 * This file is part of Mandelbulber.
 *
 * Mandelbulber is free software: you can redistribute it and/or modify it under the terms of the
 * GNU General Public License as published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * Mandelbulber is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 * without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *
 * See the GNU General Public License for more details. You should have received a copy of the GNU
 * General Public License along with Mandelbulber. If not, see <http://www.gnu.org/licenses/>.
 *
 * Authors: Krzysztof Marczak (buddhi1980@gmail.com)
 */


#include "one_parameter.hpp"

using namespace parameterContainer;

cOneParameter::cOneParameter()
{
	morphType = morphNone;
	parType = paramStandard;
	limitsDefined = false;
	isEmpty = true;
}

cOneParameter::~cOneParameter()
{
}

//set parameter value
template<class T>
void cOneParameter::Set(T val, enumValueSelection selection)
{
	switch(selection)
	{
		case valueActual:
			actualVal.Store(val);
			LimitValue(actualVal);
			break;
		case valueDefault:
			defaultVal.Store(val);
			break;
		case valueMin:
			minVal.Store(val);
			limitsDefined = true;
			break;
		case valueMax:
			maxVal.Store(val);
			limitsDefined = true;
			break;
	}
	isEmpty = false;
}
template void cOneParameter::Set<double>(double val, enumValueSelection selection);
template void cOneParameter::Set<int>(int val, enumValueSelection selection);
template void cOneParameter::Set<QString>(QString val, enumValueSelection selection);
template void cOneParameter::Set<CVector3>(CVector3 val, enumValueSelection selection);
template void cOneParameter::Set<sRGB>(sRGB val, enumValueSelection selection);
template void cOneParameter::Set<bool>(bool val, enumValueSelection selection);
template void cOneParameter::Set<cColorPalette>(cColorPalette val, enumValueSelection selection);

//get parameter value
template<class T>
T cOneParameter::Get(enumValueSelection selection) const
{
	T val = T();
	actualVal.Get(val);

	switch(selection)
	{
		case valueActual:
			actualVal.Get(val);
			break;
		case valueDefault:
			defaultVal.Get(val);
			break;
		case valueMin:
			minVal.Get(val);
			break;
		case valueMax:
			maxVal.Get(val);
			break;
	}
	return val;
}
template double cOneParameter::Get<double>(enumValueSelection selection) const;
template int cOneParameter::Get<int>(enumValueSelection selection) const;
template QString cOneParameter::Get<QString>(enumValueSelection selection) const;
template CVector3 cOneParameter::Get<CVector3>(enumValueSelection selection) const;
template sRGB cOneParameter::Get<sRGB>(enumValueSelection selection) const;
template bool cOneParameter::Get<bool>(enumValueSelection selection) const;
template cColorPalette cOneParameter::Get<cColorPalette>(enumValueSelection selection) const;

bool cOneParameter::isDefaultValue() const
{
	return (actualVal == defaultVal);
}

cMultiVal cOneParameter::GetMultival(enumValueSelection selection)
{
	switch(selection)
	{
		case valueActual:
			return actualVal;
		case valueDefault:
			return defaultVal;
		case valueMin:
			return minVal;
		case valueMax:
			return maxVal;
	}
	return actualVal;
}

void cOneParameter::SetMultival(cMultiVal multi, enumValueSelection selection)
{
	switch(selection)
	{
		case valueActual:
			actualVal = multi;
			break;
		case valueDefault:
			defaultVal = multi;
			break;
		case valueMin:
			minVal = multi;
			break;
		case valueMax:
			maxVal = multi;
			break;
	}
	isEmpty = false;
}

void cOneParameter::LimitValue(cMultiVal &multi)
{
	enumVarType varType = multi.GetDefaultype();
	switch(varType)
	{
		case typeInt:
		{
			if(limitsDefined)
			{
				int min = Get<int>(valueMin);
				int max = Get<int>(valueMax);
				int act = Get<int>(valueActual);
				if(act < min) multi.Store(min);
				if(act > max) multi.Store(max);
			}
			break;
		}
		case typeDouble:
		{
			if(limitsDefined)
			{
				double min = Get<double>(valueMin);
				double max = Get<double>(valueMax);
				double act = Get<double>(valueActual);
				if(act < min) multi.Store(min);
				if(act > max) multi.Store(max);
			}
			break;
		}
		case typeRgb:
		{
			sRGB actLimited = Get<sRGB>(valueActual);
			if(actLimited.R < 0) actLimited.R = 0;
			if(actLimited.R > 65535) actLimited.R = 65535;
			if(actLimited.G < 0) actLimited.G = 0;
			if(actLimited.G > 65535) actLimited.G = 65535;
			if(actLimited.B < 0) actLimited.B = 0;
			if(actLimited.B > 65535) actLimited.B = 65535;
			multi.Store(actLimited);
			break;
		}
		default:
			break;
	}

}
