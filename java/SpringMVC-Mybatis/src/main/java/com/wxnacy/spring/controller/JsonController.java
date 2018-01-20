package com.wxnacy.spring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.HashMap;
import java.util.Map;

@Controller
public class JsonController {

	@RequestMapping(value="/api")
    @ResponseBody
	public Map api() {
		Map map=new HashMap();
		map.put("status", "200");
		return map;
	}
}
